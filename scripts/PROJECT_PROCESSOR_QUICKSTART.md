# Quick Start - MESGRO Project Processor

**TL;DR - Get Started in 2 Minutes**

## Setup

```bash
cd scripts
```

## Option A: Generate Context Files (Free, No API Needed)

```bash
python project_processor.py "C:\path\to\your\project"
```

**Result:** Two files created
- `llm_prompt.txt` - Copy this text into ChatGPT/Claude
- `project_context.json` - Metadata for your project

## Option B: Auto-Generate Markdown (Requires OpenAI API)

```bash
pip install openai
python project_processor.py "C:\path\to\your\project" --output "output.md" --api_key "sk-..." --use-llm
```

**Result:** Complete `output.md` ready for MESGRO

---

## Prepare Your Project Folder

```
your-project/
├── report.txt          ← Project description (English or Spanish)
├── images/
│   ├── featured.jpg    ← Main image
│   └── ...
├── models/             ← 3D models (.gltf, .stl, etc)
│   └── ...
└── schematics/         ← Circuit diagrams (.svg, .pdf, etc)
    └── ...
```

---

## Workflow

### Manual (with any LLM)

1. Run: `python project_processor.py "your-project"`
2. Open `llm_prompt.txt`
3. Copy entire content
4. Paste into ChatGPT / Claude / Gemini
5. Copy the markdown response
6. Save as `_projects/project-name.md`

### Automated (OpenAI API)

1. Get API key from https://platform.openai.com/api-keys
2. Run: `python project_processor.py "your-project" --output "out.md" --api_key "sk-..." --use-llm`
3. Move `out.md` to `_projects/project-name.md`

---

## File Formats Supported

| Type | Formats |
|------|---------|
| Images | `.jpg`, `.png`, `.gif`, `.webp`, `.bmp` |
| 3D Models | `.gltf`, `.glb`, `.stl`, `.obj`, `.step`, `.stp` |
| Schematics | `.svg`, `.pdf`, `.png`, `.jpg` |
| Videos | `.mp4`, `.webm`, `.mov`, `.avi`, `.mkv` |
| Reports | `.txt`, `.md`, `.docx`, `.pdf` |

---

## Command Options

```bash
python project_processor.py <folder>              # Basic scan
python project_processor.py <folder> --output x.md # With output name
  --api_key "sk-..." --use-llm                    # Use OpenAI API
```

---

## Common Issues

| Problem | Solution |
|---------|----------|
| Report not found | Name it `report.txt` or put in root folder |
| No files found | Check folder structure and file extensions |
| API error | Check OpenAI API key and account credits |
| Markdown incomplete | Report needs more details or use GPT-4 |

---

## Next Steps

1. **Read full docs**: `PROJECT_PROCESSOR_README.md`
2. **See examples**: `PROJECT_PROCESSOR_EXAMPLES.py`
3. **Check source**: `project_processor.py`

---

For help: Run `python project_processor.py --help`
