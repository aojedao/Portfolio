# 🎨 MESGRO Project Processor - Visual Guide

## System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     YOUR PROJECT FOLDER                         │
│  ┌──────────┐  ┌─────────┐  ┌────────┐  ┌────────────┐        │
│  │ report.  │  │ images/ │  │ models/│  │ schematics/│        │
│  │   txt    │  │         │  │        │  │            │        │
│  │(English  │  │ *.jpg   │  │*.gltf  │  │  *.svg     │        │
│  │ Spanish) │  │ *.png   │  │*.stl   │  │  *.pdf     │        │
│  └──────────┘  └─────────┘  └────────┘  └────────────┘        │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│           project_processor.py (Main Script)                    │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ ProjectScanner                                           │  │
│  │ • Finds all files recursively                           │  │
│  │ • Categorizes by type (image, model, schematic)         │  │
│  │ • Reads report file                                      │  │
│  │ • Detects language (English/Spanish)                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                         │                                        │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ LLMContextGenerator                                      │  │
│  │ • Builds comprehensive LLM prompt                        │  │
│  │ • Formats file references                               │  │
│  │ • Creates JSON context                                  │  │
│  │ • Prepares MESGRO template                             │  │
│  └──────────────────────────────────────────────────────────┘  │
│                         │                                        │
│           ┌─────────────┴──────────────┐                        │
│           ▼                            ▼                        │
│   ┌──────────────────┐        ┌────────────────┐               │
│   │ llm_prompt.txt   │        │ context.json   │               │
│   │ (2000 chars)     │        │ (structured    │               │
│   │ Ready for any    │        │  data)         │               │
│   │ LLM system       │        │ (for tracking) │               │
│   └──────────────────┘        └────────────────┘               │
└────────────────────┬────────────────────────┬─────────────────┘
                     │                        │
          ┌──────────┴──────────┐             │
          │                     │             │
          ▼                     ▼             ▼
    ┌─────────────┐        ┌──────────┐  ┌──────────┐
    │  MANUAL     │        │  OPENAI  │  │   USE    │
    │  WORKFLOW   │        │   API    │  │   JSON   │
    │             │        │ (AUTO)   │  │ (TRACK)  │
    │ ChatGPT/    │        │          │  │          │
    │ Claude/     │        │Generate  │  │Archive   │
    │ Gemini      │        │markdown  │  │metadata  │
    │             │        │directly  │  │          │
    │ Copy prompt │        │          │  │          │
    │ Paste input │        │          │  │          │
    │ Get output  │        │          │  │          │
    └─────┬───────┘        └────┬─────┘  └──────────┘
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
            ┌─────────────────────┐
            │  output.md          │
            │  (MESGRO Formatted) │
            │                     │
            │ • YAML Front Matter │
            │ • Project Overview  │
            │ • Features          │
            │ • Technical Details │
            │ • Code Examples     │
            │ • File References   │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │  MESGRO STRUCTURE   │
            │                     │
            │ _projects/          │
            │ └─ project.md       │
            │                     │
            │ assets/             │
            │ ├─ images/          │
            │ ├─ models/          │
            │ └─ schematics/      │
            │                     │
            │ GitHub Pages        │
            │ (Automatic rebuild) │
            └─────────────────────┘
```

---

## Workflow Options

### Option A: Manual (No API)
```
Project Folder
    │
    ▼
project_processor.py
    │
    ├──► llm_prompt.txt
    │
    ▼
ChatGPT / Claude / Gemini
    │
    ▼ (Copy markdown response)
    │
output.md
    │
    ▼
_projects/ folder
    │
    ▼
GitHub Pages (automatic rebuild)
```

**Time:** 5-10 minutes | **Cost:** Free | **Control:** Full

---

### Option B: Automated (OpenAI API)
```
Project Folder
    │
    ▼
project_processor.py --use-llm --api_key "sk-..."
    │
    ▼
OpenAI GPT-4
    │
    ▼
output.md (already generated)
    │
    ▼
_projects/ folder
    │
    ▼
GitHub Pages (automatic rebuild)
```

**Time:** 2 minutes | **Cost:** ~$0.10-0.50 | **Control:** Minimal

---

## File Type Recognition

```
Project Folder Scanner
    │
    ├─► .jpg, .png, .gif, .webp, .bmp
    │   └─► Category: IMAGE
    │       └─► Location: images/
    │
    ├─► .gltf, .glb, .stl, .obj, .step, .stp
    │   └─► Category: 3D MODEL
    │       └─► Location: models/
    │
    ├─► .svg, .pdf, .png, .jpg (in schematics/)
    │   └─► Category: SCHEMATIC
    │       └─► Location: schematics/
    │
    ├─► .mp4, .webm, .mov, .avi, .mkv
    │   └─► Category: VIDEO
    │       └─► Location: videos/
    │
    └─► .txt, .md, .pdf, .docx (with "report" in name)
        └─► Category: REPORT
            └─► Action: Read & detect language
```

---

## Language Detection

```
Report File Content
    │
    ▼
Keyword Analysis
    │
    ├─► Spanish Keywords Detected (>10%):
    │   • el, la, de, del, que, proyecto
    │   • descripción, características
    │   • implementación, resultados
    │   │
    │   └─► LANGUAGE = "es" (Spanish)
    │       │
    │       ▼
    │       Include in LLM prompt with note:
    │       "This is a Spanish project report.
    │        Translate to English in markdown."
    │
    └─► No Spanish Keywords:
        │
        └─► LANGUAGE = "en" (English)
            │
            ▼
            Use content as-is in LLM prompt
```

---

## Generated Files Structure

```
After Running: python project_processor.py "my-project"

my-project/ (Original)
├── report.txt
├── images/
├── models/
└── schematics/

Creates:
├── project_context.json
│   {
│       "project_name": "my-project",
│       "report_language": "es",
│       "files": {
│           "images": [...],
│           "models": [...],
│           ...
│       }
│   }
│
├── llm_prompt.txt
│   (2000+ characters)
│   Ready to copy into ChatGPT/Claude
│
└── my-project.md (if --output specified + --use-llm)
    ---
    layout: project
    title: "..."
    ...
    ---
    # Project Overview
    ...
```

---

## Data Flow: Spanish Project Example

```
Input: reporte.txt (Spanish)
│
│   "Proyecto: Robot Seguidor de Línea
│    Este sistema utiliza sensores infrarojos..."
│
▼
ProjectScanner
├─► Read: report.txt
├─► Scan: Spanish keywords
├─► Detect: language = "es"
│
▼
LLMContextGenerator
├─► Build prompt with:
│   • Spanish report content
│   • "Translate to English"
│   • MESGRO template structure
│   • File references
│
├─► Generate:
│   ├─ llm_prompt.txt
│   └─ context.json
│
▼
LLM Processing
├─► Input: Comprehensive prompt with Spanish content
├─► Processing: 
│   - Understand Spanish
│   - Generate English content
│   - Follow MESGRO format
├─► Output: Complete English markdown
│
▼
Output: my-project.md (English, MESGRO-compliant)
```

---

## Command Line Interface

```bash
python project_processor.py [OPTIONS] PROJECT_PATH

┌─ Required ─────────────────────────────────────┐
│ PROJECT_PATH: Path to your project folder      │
└────────────────────────────────────────────────┘

┌─ Options ──────────────────────────────────────┐
│                                                │
│ -o, --output FILE                              │
│   Save markdown to FILE                        │
│   Example: -o "robot.md"                       │
│                                                │
│ -k, --api_key KEY                              │
│   OpenAI API key for LLM                       │
│   Example: -k "sk-proj-abc123..."              │
│                                                │
│ --use-llm                                      │
│   Enable OpenAI LLM processing                 │
│   (requires --api_key)                         │
│                                                │
│ --context-only                                 │
│   Only generate context, skip processing       │
│                                                │
│ -h, --help                                     │
│   Show help message                            │
│                                                │
└────────────────────────────────────────────────┘

Examples:
  python project_processor.py "C:\projects\robot"
  python project_processor.py "robot" -o "robot.md"
  python project_processor.py "robot" \
    -k "sk-..." --use-llm -o "robot.md"
```

---

## Processing Steps Detailed

```
STEP 1: SCANNING (30 seconds)
┌───────────────────────────────────────┐
│ Walk through project folder           │
│ • Find: images, models, schematics    │
│ • Find: report file                   │
│ • Count: files discovered             │
│ • Detect: language                    │
└────────────────┬──────────────────────┘
                 │
                 ▼
STEP 2: CATEGORIZATION (instant)
┌───────────────────────────────────────┐
│ Organize found files                  │
│ • Group by type                       │
│ • Create relative paths               │
│ • Build file lists                    │
│ • Structure context object            │
└────────────────┬──────────────────────┘
                 │
                 ▼
STEP 3: PROMPT GENERATION (instant)
┌───────────────────────────────────────┐
│ Create LLM prompt                     │
│ • Embed file references               │
│ • Include report content              │
│ • Add template structure              │
│ • Format for readability              │
└────────────────┬──────────────────────┘
                 │
        ┌────────┴─────────┐
        │                  │
        ▼                  ▼
STEP 4A: SAVE FILES    STEP 4B: LLM CALL
(instant)               (10-30 seconds)
┌──────────────┐      ┌──────────────┐
│ Save:        │      │ Send to:     │
│ • prompt.txt │      │ OpenAI API   │
│ • context    │      │              │
│   .json      │      │ Return:      │
└──────────────┘      │ markdown     │
                      └──────────────┘
                            │
                            ▼
STEP 5: FINALIZE (instant)
┌───────────────────────────────────────┐
│ Output complete                       │
│ • markdown file (if using LLM)        │
│ • context JSON file                   │
│ • prompt text file                    │
│ • Status message                      │
└───────────────────────────────────────┘
```

---

## Success Indicators

```
✅ SUCCESS SIGNS:

┌─ File Scanning ─────────────────────┐
│ ✓ Found 3+ images                   │
│ ✓ Found 1+ models/schematics        │
│ ✓ Found report file                 │
│ ✓ Language detected correctly        │
└─────────────────────────────────────┘

┌─ Context Generation ────────────────┐
│ ✓ llm_prompt.txt created (1000+KB)  │
│ ✓ context.json created              │
│ ✓ All files referenced in prompt    │
└─────────────────────────────────────┘

┌─ Markdown Generation ───────────────┐
│ ✓ Output includes YAML front matter │
│ ✓ Title present                     │
│ ✓ Description present               │
│ ✓ File references working           │
│ ✓ Code blocks formatted             │
└─────────────────────────────────────┘
```

---

## Integration Points

```
Your System
    │
    ├─► GitHub Desktop / Git CLI
    │   └─► Commit markdown to repo
    │
    ├─► GitHub Pages
    │   └─► Auto-rebuild site
    │
    ├─► ChatGPT / Claude UI
    │   └─► Paste prompt for markdown
    │
    ├─► OpenAI API
    │   └─► Auto-generate markdown
    │
    ├─► Batch Scripts
    │   └─► Process multiple projects
    │
    └─► GitHub Actions
        └─► Automated CI/CD pipeline
```

---

**This system integrates seamlessly with your MESGRO portfolio workflow!**
