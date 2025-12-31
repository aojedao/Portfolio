"""
MESGRO Project Processor - Usage Examples

This file demonstrates various ways to use the project_processor.py script
for converting project folders to MESGRO markdown format.
"""

# ==============================================================================
# EXAMPLE 1: Basic Context Generation (No LLM)
# ==============================================================================

"""
Use case: You want to prepare context files but will manually create the markdown

Command:
    cd scripts
    python project_processor.py "../projects/my-robot-v1"

This generates:
- project_context.json      # Machine-readable project data
- llm_prompt.txt           # Human/LLM-readable prompt for markdown generation

Output:
    🔍 Scanning project: ../projects/my-robot-v1
    ✅ Found:
       - 8 images
       - 4 3D models
       - 3 schematics
       - 2 videos
       - Report language: Spanish
    📋 Context saved to: project_context.json
    🤖 LLM prompt saved to: llm_prompt.txt
    ✅ Status: ready_for_llm

Next step:
    1. Copy content from llm_prompt.txt
    2. Paste into ChatGPT, Claude, or Gemini
    3. Get the markdown response
    4. Save as _projects/my-robot-v1.md
"""


# ==============================================================================
# EXAMPLE 2: Automatic Markdown Generation with OpenAI
# ==============================================================================

"""
Use case: Full automation - scan, prompt, generate, and save

Prerequisites:
    pip install openai

Command:
    cd scripts
    python project_processor.py "../projects/iot-sensor-network" \
        --output "iot-sensor.md" \
        --api_key "sk-proj-abc123..." \
        --use-llm

This generates:
- iot-sensor.md            # Complete MESGRO-formatted markdown
- iot-sensor_context.json  # Project context for reference
- iot-sensor_prompt.txt    # The prompt that was sent to LLM

Output:
    🔍 Scanning project: ../projects/iot-sensor-network
    ✅ Found:
       - 6 images
       - 3 3D models
       - 4 schematics
       - 1 videos
       - Report language: English
    🤖 Sending to LLM for processing...
    ✅ LLM processing complete
    📄 Markdown saved to: iot-sensor.md
    📋 Context saved to: iot-sensor_context.json
    🤖 LLM prompt saved to: iot-sensor_prompt.txt
    ✅ Status: llm_processed

Next steps:
    1. Review iot-sensor.md for accuracy
    2. Make any necessary edits
    3. Copy images to assets/images/projects/iot-sensor-network/
    4. Copy models to assets/models/projects/iot-sensor-network/
    5. Copy schematics to assets/schematics/projects/iot-sensor-network/
    6. Move iot-sensor.md to _projects/
    7. Commit and push to GitHub
"""


# ==============================================================================
# EXAMPLE 3: Processing Multiple Projects Sequentially
# ==============================================================================

"""
Use case: You have multiple projects to add to the portfolio

Script approach - create a batch processor:
"""

import subprocess
import json
from pathlib import Path

def batch_process_projects(projects_dir, output_dir, api_key=None):
    """
    Process all project folders in a directory
    
    Folder structure expected:
    projects/
        ├── robot-1/
        │   ├── report.txt
        │   ├── images/
        │   ├── models/
        │   └── schematics/
        ├── robot-2/
        │   └── [same structure]
        └── robot-3/
            └── [same structure]
    """
    projects_dir = Path(projects_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    results = []
    
    for project_folder in sorted(projects_dir.iterdir()):
        if not project_folder.is_dir():
            continue
        
        print(f"\n{'='*60}")
        print(f"Processing: {project_folder.name}")
        print(f"{'='*60}")
        
        cmd = [
            "python", "project_processor.py",
            str(project_folder),
            "-o", str(output_dir / f"{project_folder.name}.md")
        ]
        
        if api_key:
            cmd.extend(["--api_key", api_key, "--use-llm"])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(result.stdout)
            results.append({
                "project": project_folder.name,
                "status": "success",
                "output": str(output_dir / f"{project_folder.name}.md")
            })
        except subprocess.CalledProcessError as e:
            print(f"❌ Error processing {project_folder.name}")
            print(e.stderr)
            results.append({
                "project": project_folder.name,
                "status": "error",
                "error": str(e)
            })
    
    # Save summary
    summary_file = output_dir / "processing_summary.json"
    with open(summary_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Summary saved to: {summary_file}")
    print(f"{'='*60}")

# Usage:
# batch_process_projects("projects/", "output/", api_key="sk-...")


# ==============================================================================
# EXAMPLE 4: Spanish Project Report (Automatic Translation)
# ==============================================================================

"""
Use case: Project report is in Spanish, needs to be converted to English markdown

Folder structure:
    proyecto-brazo-robotico/
    ├── reporte.txt
    │   (contains: "Este proyecto implementa un brazo robótico de 6 DOF...")
    ├── imagenes/
    │   ├── ensamble.jpg
    │   └── funcionando.jpg
    ├── modelos/
    │   ├── base.gltf
    │   ├── link1.gltf
    │   └── gripper.gltf
    └── esquematicos/
        ├── motor-control.svg
        └── power-supply.svg

Command:
    cd scripts
    python project_processor.py "../proyecto-brazo-robotico" \
        --output "robotic-arm.md" \
        --api_key "sk-proj-xyz..." \
        --use-llm

The processor will:
1. ✅ Detect Spanish language in reporte.txt
2. ✅ Extract project information
3. ✅ Create an LLM prompt that includes the Spanish text
4. ✅ LLM translates and creates English markdown
5. ✅ Generate proper MESGRO format

Result: robotic-arm.md with English content and proper template structure
"""


# ==============================================================================
# EXAMPLE 5: Manual LLM Processing (Copy-Paste)
# ==============================================================================

"""
Use case: You don't have API access but want to use an LLM manually

Workflow:

Step 1: Generate the prompt
    cd scripts
    python project_processor.py "../my-project"

Step 2: Open llm_prompt.txt (should be ~100-150 lines)

Step 3: Copy entire content of llm_prompt.txt

Step 4: Go to ChatGPT/Claude/Gemini and start a new conversation

Step 5: Paste the prompt

Step 6: The LLM will generate a complete markdown file

Step 7: Copy the markdown from the LLM response

Step 8: Create a new file in _projects/ and paste the content
    
Step 9: Verify paths match your asset folders

Step 10: Commit and push

Files generated:
    project_context.json    - Use if you want to track metadata
    llm_prompt.txt         - The prompt you copied
"""


# ==============================================================================
# EXAMPLE 6: Advanced - Custom Processing Script
# ==============================================================================

"""
Use case: You want more control over the process or need custom logic

Example script that extends the processor:
"""

from project_processor import ProjectScanner, LLMContextGenerator

def custom_processing():
    """
    Custom workflow with additional processing
    """
    # Scan the project
    scanner = ProjectScanner("../my-project")
    context = scanner.scan()
    
    # Custom filtering - only include recent images
    from datetime import datetime, timedelta
    recent = datetime.now() - timedelta(days=30)
    context.images = [
        img for img in context.images 
        if datetime.fromtimestamp(Path(img.path).stat().st_mtime) > recent
    ]
    
    # Generate context
    generator = LLMContextGenerator(context)
    
    # Custom modifications to prompt
    prompt = generator.generate_llm_prompt()
    
    # Add custom instructions
    custom_instruction = """
    
ADDITIONAL INSTRUCTIONS:
- Focus on the electrical subsystem
- Emphasize the sensor integration
- Include a troubleshooting section
- Add a bill of materials (BOM) section
"""
    prompt += custom_instruction
    
    # Save modified prompt
    with open("custom_prompt.txt", 'w') as f:
        f.write(prompt)
    
    print("Custom prompt saved to custom_prompt.txt")
    print(f"Modified prompt length: {len(prompt)} characters")

# Usage:
# custom_processing()


# ==============================================================================
# EXAMPLE 7: Project Folder Structure Best Practices
# ==============================================================================

"""
For best results with the processor, organize your project like this:

Minimal Structure:
    my-project/
    ├── report.txt
    └── images/
        └── featured.jpg

Recommended Structure:
    my-project/
    ├── report.txt
    ├── images/
    │   ├── featured.jpg
    │   ├── assembly.jpg
    │   ├── testing.jpg
    │   └── final-result.jpg
    ├── models/
    │   ├── main-body.gltf
    │   ├── wheel.gltf
    │   └── electronics-mount.gltf
    └── schematics/
        ├── main-circuit.svg
        ├── power-distribution.svg
        └── sensor-interface.svg

Complete Structure:
    my-project/
    ├── report.txt                     # Project description
    ├── images/
    │   ├── featured.jpg               # Used as main image
    │   ├── assembly/
    │   │   ├── step1.jpg
    │   │   ├── step2.jpg
    │   │   └── step3.jpg
    │   └── results/
    │       ├── demo1.jpg
    │       └── demo2.jpg
    ├── models/                        # CAD Models (GLTF/STL)
    │   ├── chassis.gltf
    │   ├── motor-mount.gltf
    │   ├── arm-segment.gltf
    │   └── original-cad/              # For reference
    │       └── assembly.step
    ├── schematics/                    # Circuit Diagrams
    │   ├── motor-driver.svg
    │   ├── power-management.svg
    │   ├── sensor-board.svg
    │   └── overall-system.svg
    └── videos/                        # Optional demo videos
        ├── assembly.mp4
        └── final-demo.mp4

Notes:
- Put the most important image as featured.jpg (256x256 or larger)
- Use descriptive names for 3D models
- Include SVG versions of schematics for best web display
- Keep report.txt clear and organized
"""


# ==============================================================================
# EXAMPLE 8: Troubleshooting & Tips
# ==============================================================================

"""
Common Issues and Solutions:

1. "Report not found"
   - Ensure report file is in the root of the project folder
   - Supported names: report.txt, report.md, project_report.*
   - Must have report, report_*, or project_report* in the filename

2. "No files found"
   - Check folder structure is correct
   - Verify files have the right extensions (see supported lists)
   - Try: python project_processor.py "path" --verbose

3. "LLM processing failed"
   - Check API key is correct
   - Verify OpenAI account has access
   - Check network connection
   - Try again in a few minutes (API rate limits)

4. "Generated markdown is incomplete"
   - Report might lack detail
   - Try with GPT-4 model (more comprehensive)
   - Manually enhance based on the context JSON
   - Use llm_prompt.txt with a different LLM

5. "File paths are wrong in generated markdown"
   - The processor generates relative paths
   - Adjust folder names in the markdown if needed
   - Ensure assets are in correct folders before copying

Tips:
- Always review generated markdown before publishing
- Test 3D models render correctly in the browser
- Verify all image and model paths work
- Use the context JSON for documentation
- Keep the llm_prompt.txt for future reference
"""


# ==============================================================================
# EXAMPLE 9: Integration with CI/CD Pipeline
# ==============================================================================

"""
Use in GitHub Actions or GitLab CI to automate project creation:

GitHub Actions Workflow (.github/workflows/process-projects.yml):

name: Process Projects

on:
  push:
    paths:
      - 'projects/**'
  workflow_dispatch:

jobs:
  process:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install openai
      
      - name: Process projects
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          cd scripts
          for project in ../projects/*/; do
            python project_processor.py "$project" \\
              --api_key "$OPENAI_API_KEY" \\
              --use-llm \\
              --output "../_projects/$(basename $project).md"
          done
      
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add _projects/
          git commit -m "Auto-generate project markdown"
          git push

This automatically:
1. Detects new project folders pushed
2. Runs processor on each
3. Generates markdown files
4. Commits them to the repo
5. Jekyll rebuilds the site automatically
"""


# ==============================================================================
# EXAMPLE 10: Output File Reference
# ==============================================================================

"""
Generated Files Explanation:

1. project.md (if --output specified)
   - Complete MESGRO-formatted markdown
   - Ready to move to _projects/ folder
   - Use as-is or customize before deploying

2. project_context.json
   - Machine-readable project metadata
   - Lists all found files with paths
   - Useful for scripts or tracking
   - Example structure:
     {
       "project_name": "my-robot",
       "report_language": "es",
       "media_count": {
         "images": 5,
         "models": 3,
         "schematics": 2,
         "videos": 1
       },
       "files": { ... }
     }

3. project_prompt.txt
   - The exact prompt sent to the LLM
   - Contains all project context
   - Useful for debugging or using with different LLM
   - ~3000-5000 characters typically

What to do with each:
- markdown file: Move to _projects/
- context JSON: Keep for reference or archival
- prompt text: Keep for re-running with different LLM
"""

print(__doc__)
