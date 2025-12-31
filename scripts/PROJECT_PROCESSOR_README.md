# 🤖 MESGRO Project Processor

An intelligent LLM context file that automatically processes project folders and converts them to MESGRO-compliant markdown files.

## 🎯 What It Does

The **Project Processor** is designed to:

1. **Scan** a project folder for all media files:
   - Images (JPG, PNG, GIF, WebP, BMP)
   - 3D Models (GLTF, GLB, STL, OBJ, STEP)
   - Schematics (SVG, PDF, PNG)
   - Videos (MP4, WebM, MOV, AVI, MKV)

2. **Read** project reports (in English or Spanish)
3. **Detect** the report language automatically
4. **Generate** a comprehensive LLM prompt that includes:
   - All media file references
   - Project context
   - The original report content
   - MESGRO template structure

5. **Optionally** use OpenAI's API to automatically generate the final markdown

## 📁 Folder Structure

Create a folder with your project files like this:

```
my-awesome-project/
├── report.txt                    # 📝 Project description (English or Spanish)
├── images/
│   ├── featured.jpg             # Main project image
│   ├── assembly.jpg
│   └── working.jpg
├── models/
│   ├── chassis.gltf
│   ├── wheel.gltf
│   └── arm.stl
├── schematics/
│   ├── main-circuit.svg
│   ├── power.svg
│   └── motor-control.svg
└── videos/
    ├── demo.mp4
    └── assembly.mp4
```

The report file can be named:
- `report.txt`
- `report.md`
- `project_report.docx` (requires `python-docx`)
- `project_report.pdf` (requires `pdfplumber`)

## 🚀 Quick Start

### Option 1: Generate Context Only (No LLM Required)

```bash
cd scripts
python project_processor.py "../path/to/my-project"
```

This generates:
- `project_context.json` - Structured data about your project
- `llm_prompt.txt` - The prompt ready for any LLM

### Option 2: Auto-Generate Markdown with OpenAI

First, install the OpenAI package:

```bash
pip install openai
```

Then run:

```bash
python project_processor.py "../path/to/my-project" \
  --output "generated_project.md" \
  --api_key "sk-your-openai-key" \
  --use-llm
```

This generates:
- `generated_project.md` - Complete, ready-to-use project markdown
- `generated_project_context.json` - Context data
- `generated_project_prompt.txt` - The LLM prompt used

## 💻 Command-Line Options

```bash
python project_processor.py <project_path> [options]

Arguments:
  project_path              Path to the project folder (required)

Options:
  -o, --output FILE         Save generated markdown to FILE
  -k, --api_key KEY         OpenAI API key for LLM processing
  --use-llm                 Enable LLM processing (requires --api_key)
  --context-only            Only generate context, don't process
  -h, --help                Show this help message
```

## 📋 Examples

### Example 1: Basic Scan
```bash
python project_processor.py "C:/projects/my-robot"
```

**Output:**
```
🔍 Scanning project: C:/projects/my-robot
✅ Found:
   - 5 images
   - 3 3D models
   - 2 schematics
   - 1 videos
   - Report language: Spanish
📋 Context saved to: project_context.json
🤖 LLM prompt saved to: llm_prompt.txt
✅ Status: ready_for_llm
```

### Example 2: Generate Markdown with LLM
```bash
python project_processor.py "C:/projects/my-robot" \
  --output "robot.md" \
  --api_key "sk-proj-abc123..." \
  --use-llm
```

**Output:**
```
🔍 Scanning project: C:/projects/my-robot
✅ Found:
   - 5 images
   - 3 3D models
   - 2 schematics
   - 1 videos
   - Report language: Spanish
🤖 Sending to LLM for processing...
✅ LLM processing complete
📄 Markdown saved to: robot.md
📋 Context saved to: robot_context.json
🤖 LLM prompt saved to: robot_prompt.txt
✅ Status: llm_processed
```

### Example 3: Copy and Paste Prompt into ChatGPT

If you don't have an API key, you can use the generated prompt manually:

```bash
python project_processor.py "C:/projects/my-robot"
```

Then:
1. Open `llm_prompt.txt`
2. Copy the entire content
3. Paste into ChatGPT or Claude
4. Get the generated markdown and save as `project.md`
5. Move to `_projects/` folder

## 🔄 Workflow with MESGRO

### Step 1: Prepare Your Project Folder

Create a folder with your project files:
```
research-project/
├── report.txt            (Your project description)
├── images/               (Photos of your project)
├── models/               (3D CAD models as GLTF/STL)
└── schematics/           (Circuit diagrams as SVG/PDF)
```

### Step 2: Run the Processor

```bash
python scripts/project_processor.py "research-project" \
  --output "research.md" \
  --api_key "sk-..." \
  --use-llm
```

### Step 3: Review and Customize

The generated `research.md` will be in the MESGRO format. Review it and make any adjustments.

### Step 4: Deploy

1. Copy images to `assets/images/projects/project-name/`
2. Copy models to `assets/models/projects/project-name/`
3. Copy schematics to `assets/schematics/projects/project-name/`
4. Move markdown to `_projects/project-name.md`
5. Update paths in the markdown if necessary
6. Push to GitHub and the Jekyll site updates automatically!

## 🌐 Multi-Language Support

The processor **automatically detects** Spanish or English reports.

### Spanish Report Example:

```txt
Proyecto: Robot Seguidor de Línea

Descripción General:
Este proyecto implementa un robot autónomo capaz de seguir una línea negra
sobre un fondo blanco utilizando sensores infrarojos y control PID.

Características:
- Control PID para seguimiento preciso
- 5 sensores infrarojos
- Motores DC con retroalimentación de encoder
```

The processor will:
1. ✅ Detect it's Spanish
2. ✅ Extract key information
3. ✅ Translate technical terms to English
4. ✅ Generate the markdown with translations

## 📦 Dependencies

### Required
- Python 3.8+
- Standard library only for basic functionality

### Optional
- `openai` - For automated LLM processing
  ```bash
  pip install openai
  ```
- `pdfplumber` - For PDF report reading
  ```bash
  pip install pdfplumber
  ```
- `python-docx` - For DOCX report reading
  ```bash
  pip install python-docx
  ```

## 🎨 MESGRO Template Structure

The processor generates markdown following this structure:

```yaml
---
layout: project
title: "Project Title"
description: "Brief description"
date: YYYY-MM-DD
categories: [Category1, Category2]
featured_image: "/assets/images/projects/project-slug/featured.jpg"
github_url: "https://github.com/..."
demo_url: "https://demo.com"

models:
  - file: "/assets/models/projects/project-slug/model.gltf"
    description: "Model description"

schematics:
  - file: "/assets/schematics/projects/project-slug/circuit.svg"
    description: "Schematic description"

images:
  - file: "/assets/images/projects/project-slug/image.jpg"
    alt: "Image description"
---

# Project Overview

[Content]

## Features

[Features list]

## Technical Details

[Implementation details]
```

## 🔍 File Recognition

| File Type | Extensions | Detected As |
|-----------|-----------|-------------|
| Images | `.jpg`, `.png`, `.gif`, `.webp`, `.bmp` | Image |
| 3D Models | `.gltf`, `.glb`, `.stl`, `.obj`, `.step`, `.stp` | Model |
| Schematics | `.svg`, `.pdf`, `.png`, `.jpg` | Schematic |
| Videos | `.mp4`, `.webm`, `.mov`, `.avi`, `.mkv` | Video |
| Reports | `.txt`, `.md`, `.pdf`, `.docx` | Report |

## ⚙️ How It Works

```
┌─────────────────────────┐
│   Project Folder        │
│  (with report & media)  │
└────────────┬────────────┘
             │
             ▼
    ┌────────────────┐
    │  ProjectScanner │
    │  - Find files  │
    │  - Detect lang │
    │  - Read report │
    └────────┬───────┘
             │
             ▼
    ┌──────────────────┐
    │ ProjectContext   │
    │  - Media list   │
    │  - Report text  │
    │  - Language     │
    └────────┬────────┘
             │
             ▼
    ┌──────────────────┐
    │ LLMContextGen    │
    │  - Build prompt │
    │  - Format JSON  │
    └────────┬────────┘
             │
         ┌───┴────┐
         │         │
         ▼         ▼
    Prompt.txt   JSON
         │         │
         │         └─────────┐
         │                   │
         ▼ (Optional LLM)     │
    ┌──────────┐             │
    │ OpenAI   │             │
    │ GPT-4    │             │
    └────┬─────┘             │
         │                   │
         ▼                   ▼
    Markdown           Context Data
    (project.md)       (for reference)
```

## 🤖 Using with Different LLMs

### OpenAI (Recommended)
```bash
python project_processor.py "project" --api_key "sk-..." --use-llm
```

### Claude/Manual
```bash
python project_processor.py "project"
# Copy content from llm_prompt.txt
# Paste into Claude at claude.ai
# Copy response to project.md
```

### Anthropic API
Modify the script to use Anthropic's client:
```python
from anthropic import Anthropic
client = Anthropic(api_key=api_key)
# Use client.messages.create() instead of OpenAI
```

## 🐛 Troubleshooting

### "Project path not found"
- Check the path is correct and the folder exists

### "PDF file detected but requires pdfplumber"
```bash
pip install pdfplumber
```

### "DOCX file detected but requires python-docx"
```bash
pip install python-docx
```

### "OpenAI library not found"
```bash
pip install openai
```

### "OpenAI authentication error"
- Verify your API key is correct
- Check your OpenAI account has API access enabled
- Ensure you have credits/quota remaining

### Generated markdown looks incomplete
- The report might not have enough information
- Try using GPT-4 model (more capable)
- Manually edit the generated markdown

## 📝 Manual Workflow

If you prefer not to use the LLM API:

```bash
# 1. Generate the prompt
python project_processor.py "my-project"

# 2. Open llm_prompt.txt
# 3. Copy entire content
# 4. Paste into ChatGPT / Claude / Gemini
# 5. Get the generated markdown
# 6. Save as my-project.md
# 7. Move to _projects/ folder
```

## 🎓 Examples of Generated Projects

The MESGRO template is designed for:

- **Robotics Projects**: Line-following robots, robotic arms, drones
- **IoT Systems**: Environmental monitors, sensor networks
- **Mechatronics**: Mixed hardware/software projects
- **3D Printing**: CAD designs with models and documentation
- **Electronics**: Circuit design and embedded systems

## 📖 Reference

For more information on the MESGRO format, see:
- `_projects/iot-environmental-monitor.md` - Complete example
- `_projects/line-following-robot.md` - Another example
- `_layouts/project.html` - HTML template structure

## 📄 License

This processor is part of the MESGRO project.

## 🤝 Contributing

To improve this processor:

1. Test with different project types
2. Improve language detection
3. Add support for more file formats
4. Enhance the LLM prompt for better results
5. Add support for more LLM providers

---

**Created for MESGRO - Mechanical, Electrical, Software Gallery for Robots**
