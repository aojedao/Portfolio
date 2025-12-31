#!/usr/bin/env python3
"""
MESGRO Project Processor - LLM Context File

This script serves as an intelligent agent that:
1. Scans a project folder for images, 3D models, and video files
2. Reads a project report (in English or Spanish)
3. Generates context and prompts for an LLM to create a MESGRO-compliant markdown file

Usage:
    python project_processor.py <project_folder_path> [--output <output_file>] [--api_key <openai_key>]

Example:
    python project_processor.py "C:/projects/my-robot-project"
    python project_processor.py "C:/projects/my-robot-project" --output "robot.md" --api_key "sk-..."

Dependencies:
    - Python 3.8+
    - pathlib (built-in)
    - json (built-in)
    - Optional: openai (for LLM integration)
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
import mimetypes

# Supported file extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
MODEL_EXTENSIONS = {'.gltf', '.glb', '.stl', '.obj', '.step', '.stp'}
VIDEO_EXTENSIONS = {'.mp4', '.webm', '.mov', '.avi', '.mkv'}
SCHEMATIC_EXTENSIONS = {'.svg', '.pdf', '.png', '.jpg', '.jpeg'}


@dataclass
class MediaFile:
    """Represents a media file in the project"""
    path: str
    file_type: str  # 'image', 'model', 'video', 'schematic'
    filename: str
    relative_path: str


@dataclass
class ProjectContext:
    """Represents the complete context of a project"""
    project_name: str
    report_text: str
    report_language: str  # 'en' or 'es'
    images: List[MediaFile]
    models: List[MediaFile]
    videos: List[MediaFile]
    schematics: List[MediaFile]
    other_files: List[MediaFile]


class ProjectScanner:
    """Scans a project directory for media files and report"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        if not self.project_path.exists():
            raise FileNotFoundError(f"Project path not found: {project_path}")
    
    def scan(self) -> ProjectContext:
        """
        Scan the project directory and gather all context
        Returns a ProjectContext object with all project information
        """
        images = []
        models = []
        videos = []
        schematics = []
        other_files = []
        report_text = ""
        report_language = "en"
        
        # Scan all files in the project directory
        for file_path in self.project_path.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(self.project_path)
                file_ext = file_path.suffix.lower()
                
                # Check for report files
                if file_ext in {'.txt', '.md', '.docx', '.pdf'} and 'report' in file_path.name.lower():
                    report_text, report_language = self._read_report(file_path)
                    continue
                
                # Categorize files
                if file_ext in IMAGE_EXTENSIONS:
                    images.append(MediaFile(
                        path=str(file_path),
                        file_type='image',
                        filename=file_path.name,
                        relative_path=str(relative_path)
                    ))
                elif file_ext in MODEL_EXTENSIONS:
                    models.append(MediaFile(
                        path=str(file_path),
                        file_type='model',
                        filename=file_path.name,
                        relative_path=str(relative_path)
                    ))
                elif file_ext in VIDEO_EXTENSIONS:
                    videos.append(MediaFile(
                        path=str(file_path),
                        file_type='video',
                        filename=file_path.name,
                        relative_path=str(relative_path)
                    ))
                elif file_ext in SCHEMATIC_EXTENSIONS:
                    schematics.append(MediaFile(
                        path=str(file_path),
                        file_type='schematic',
                        filename=file_path.name,
                        relative_path=str(relative_path)
                    ))
                else:
                    other_files.append(MediaFile(
                        path=str(file_path),
                        file_type='other',
                        filename=file_path.name,
                        relative_path=str(relative_path)
                    ))
        
        project_name = self.project_path.name
        
        return ProjectContext(
            project_name=project_name,
            report_text=report_text,
            report_language=report_language,
            images=images,
            models=models,
            videos=videos,
            schematics=schematics,
            other_files=other_files
        )
    
    def _read_report(self, file_path: Path) -> Tuple[str, str]:
        """
        Read project report file
        Returns (text_content, detected_language)
        """
        try:
            if file_path.suffix == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif file_path.suffix == '.md':
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif file_path.suffix == '.pdf':
                # Would require pdfplumber or similar
                # For now, return empty with note
                print(f"⚠️  PDF file detected but requires pdfplumber. Skipping: {file_path.name}")
                text = ""
            elif file_path.suffix == '.docx':
                # Would require python-docx
                print(f"⚠️  DOCX file detected but requires python-docx. Skipping: {file_path.name}")
                text = ""
            else:
                return "", "en"
            
            # Detect language (simple heuristic)
            language = self._detect_language(text)
            return text, language
        
        except Exception as e:
            print(f"Error reading report file {file_path}: {e}")
            return "", "en"
    
    def _detect_language(self, text: str) -> str:
        """
        Simple language detection based on Spanish keywords
        Returns 'es' or 'en'
        """
        spanish_keywords = {
            'el', 'la', 'los', 'las', 'de', 'del', 'un', 'una', 'unos', 'unas',
            'que', 'proyecto', 'sistema', 'robot', 'sensor', 'control', 'objetivo',
            'descripción', 'características', 'implementación', 'resultados'
        }
        
        words = re.findall(r'\b\w+\b', text.lower())
        spanish_count = sum(1 for word in words if word in spanish_keywords)
        
        # If more than 10% of words are Spanish keywords, assume Spanish
        if len(words) > 0 and spanish_count / len(words) > 0.10:
            return "es"
        return "en"


class LLMContextGenerator:
    """Generates LLM prompts and context from ProjectContext"""
    
    MESGRO_TEMPLATE = """
---
layout: project
title: "{title}"
description: "{description}"
date: {date}
categories: [{categories}]
featured_image: "/assets/images/projects/{project_slug}/featured.jpg"
github_url: "{github_url}"
demo_url: "{demo_url}"

# 3D Models - Support for STL, OBJ, GLTF, GLB formats
models:
{models}

# Circuit Schematics - PNG, JPG, SVG, PDF formats
schematics:
{schematics}

# Images
images:
{images}

# Code Files with syntax highlighting
code_files:
{code_files}

---

# Project Overview
{overview}

## Features

{features}

## Technical Details

### Components
{components}

### Architecture
{architecture}

### Implementation
{implementation}

## Results

{results}

## Files & Resources

- [Repository](https://github.com/aojedao/{project_slug})
- [Models & CAD](/assets/models/{project_slug}/)
- [Schematics](/assets/schematics/{project_slug}/)
"""
    
    def __init__(self, context: ProjectContext):
        self.context = context
    
    def generate_llm_prompt(self) -> str:
        """
        Generate a detailed prompt for an LLM to create the project markdown
        """
        prompt = f"""
You are an expert technical writer specializing in robotics and mechanical engineering projects.
Your task is to convert a project report into a well-formatted MESGRO (Mechanical, Electrical, 
Software Gallery for Robots) markdown file.

PROJECT INFORMATION:
====================

Project Name: {self.context.project_name}
Report Language: {'Spanish' if self.context.report_language == 'es' else 'English'}

AVAILABLE MEDIA FILES:
======================

Images ({len(self.context.images)} found):
{self._format_file_list(self.context.images)}

3D Models ({len(self.context.models)} found):
{self._format_file_list(self.context.models)}

Schematics ({len(self.context.schematics)} found):
{self._format_file_list(self.context.schematics)}

Videos ({len(self.context.videos)} found):
{self._format_file_list(self.context.videos)}

PROJECT REPORT (Original Language):
====================================

{self.context.report_text}

YOUR TASK:
===========

1. Read and understand the project report
2. If in Spanish, translate key information to English
3. Extract or infer:
   - Project title
   - Concise description (1-2 sentences)
   - Main features and capabilities
   - Technical components used
   - System architecture
   - Implementation approach
   - Results and achievements

4. Create a markdown file following the MESGRO template below:

MESGRO TEMPLATE:
================

{self.MESGRO_TEMPLATE}

5. Include proper references to:
   - Images: /assets/images/projects/{self._slugify(self.context.project_name)}/
   - Models: /assets/models/projects/{self._slugify(self.context.project_name)}/
   - Schematics: /assets/schematics/projects/{self._slugify(self.context.project_name)}/

6. Format code blocks with proper language tags (cpp, python, javascript, etc.)

7. Create a well-organized, professional markdown that:
   - Uses clear sections and subsections
   - Includes technical details appropriate for an engineering portfolio
   - Highlights innovative aspects of the project
   - Provides context for both technical and non-technical readers

OUTPUT FORMAT:
==============
Return ONLY the complete markdown file content, ready to be saved as a .md file.
Include the YAML front matter and all sections.
"""
        return prompt
    
    def generate_context_json(self) -> str:
        """
        Generate a JSON representation of the project context
        Useful for structured processing
        """
        context_dict = {
            'project_name': self.context.project_name,
            'report_language': self.context.report_language,
            'media_count': {
                'images': len(self.context.images),
                'models': len(self.context.models),
                'schematics': len(self.context.schematics),
                'videos': len(self.context.videos),
            },
            'files': {
                'images': [asdict(f) for f in self.context.images],
                'models': [asdict(f) for f in self.context.models],
                'schematics': [asdict(f) for f in self.context.schematics],
                'videos': [asdict(f) for f in self.context.videos],
            }
        }
        return json.dumps(context_dict, indent=2)
    
    def _format_file_list(self, files: List[MediaFile]) -> str:
        """Format a list of files for display"""
        if not files:
            return "  (none found)"
        
        result = []
        for f in files:
            result.append(f"  - {f.relative_path}")
        return "\n".join(result)
    
    def _slugify(self, text: str) -> str:
        """Convert text to URL-friendly slug"""
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')


class ProjectProcessor:
    """Main processor that orchestrates scanning and LLM interaction"""
    
    def __init__(self, project_path: str):
        self.project_path = project_path
        self.scanner = ProjectScanner(project_path)
        
    def process(self, use_llm: bool = False, api_key: Optional[str] = None) -> Dict:
        """
        Process the project and optionally use LLM
        Returns a dictionary with results
        """
        print(f"🔍 Scanning project: {self.project_path}")
        context = self.scanner.scan()
        
        print(f"✅ Found:")
        print(f"   - {len(context.images)} images")
        print(f"   - {len(context.models)} 3D models")
        print(f"   - {len(context.schematics)} schematics")
        print(f"   - {len(context.videos)} videos")
        print(f"   - Report language: {'Spanish' if context.report_language == 'es' else 'English'}")
        
        generator = LLMContextGenerator(context)
        
        results = {
            'context': context,
            'llm_prompt': generator.generate_llm_prompt(),
            'context_json': generator.generate_context_json(),
            'status': 'ready_for_llm'
        }
        
        if use_llm and api_key:
            print("🤖 Sending to LLM for processing...")
            try:
                from openai import OpenAI
                client = OpenAI(api_key=api_key)
                
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert technical writer for robotics projects."},
                        {"role": "user", "content": results['llm_prompt']}
                    ],
                    temperature=0.7,
                    max_tokens=4000
                )
                
                results['generated_markdown'] = response.choices[0].message.content
                results['status'] = 'llm_processed'
                print("✅ LLM processing complete")
            
            except ImportError:
                print("⚠️  OpenAI library not found. Install with: pip install openai")
                results['status'] = 'ready_for_llm'
            except Exception as e:
                print(f"❌ LLM processing failed: {e}")
                results['status'] = 'llm_error'
        
        return results


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='MESGRO Project Processor - Convert project folders to markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project_processor.py "C:/my-project"
  python project_processor.py "C:/my-project" --output "project.md"
  python project_processor.py "C:/my-project" --api_key "sk-..." --use-llm
        """
    )
    
    parser.add_argument('project_path', help='Path to the project folder')
    parser.add_argument('-o', '--output', help='Output markdown file path')
    parser.add_argument('-k', '--api_key', help='OpenAI API key for LLM processing')
    parser.add_argument('--use-llm', action='store_true', help='Use OpenAI LLM for processing')
    parser.add_argument('--context-only', action='store_true', help='Only generate context, don\'t process')
    
    args = parser.parse_args()
    
    try:
        processor = ProjectProcessor(args.project_path)
        results = processor.process(
            use_llm=args.use_llm,
            api_key=args.api_key
        )
        
        # Save results
        if args.output:
            if 'generated_markdown' in results:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(results['generated_markdown'])
                print(f"📄 Markdown saved to: {args.output}")
            else:
                print("❌ No markdown generated. Use --use-llm with --api_key to generate markdown.")
        
        # Save context JSON for reference
        context_json_path = args.output.replace('.md', '_context.json') if args.output else 'project_context.json'
        with open(context_json_path, 'w', encoding='utf-8') as f:
            f.write(results['context_json'])
        print(f"📋 Context saved to: {context_json_path}")
        
        # Save LLM prompt for reference
        if args.output:
            prompt_path = args.output.replace('.md', '_prompt.txt')
        else:
            prompt_path = 'llm_prompt.txt'
        with open(prompt_path, 'w', encoding='utf-8') as f:
            f.write(results['llm_prompt'])
        print(f"🤖 LLM prompt saved to: {prompt_path}")
        
        print(f"\n✅ Status: {results['status']}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
