# MESGRO Project Processor - Complete Documentation Index

## 📚 File Overview

This directory now contains a complete LLM-powered system for converting project folders into MESGRO markdown format.

### Core Files

#### 1. **project_processor.py** (Main Script)
- **Size:** ~700 lines
- **Purpose:** The main processor that scans projects, reads reports, and generates LLM prompts
- **Use:** Run this script with your project folder
- **Key Classes:**
  - `ProjectScanner` - Finds and categorizes media files
  - `LLMContextGenerator` - Creates LLM prompts from project data
  - `ProjectProcessor` - Orchestrates the entire workflow
- **Features:**
  - Automatic language detection (English/Spanish)
  - Support for multiple file formats
  - Optional OpenAI API integration
  - Context JSON generation for structured data

### Documentation Files

#### 2. **PROJECT_PROCESSOR_QUICKSTART.md** ⭐ START HERE
- **Purpose:** Quick reference guide (2-minute read)
- **Contains:**
  - Basic setup instructions
  - Two-step workflows
  - Common issues and solutions
  - File format reference

#### 3. **PROJECT_PROCESSOR_README.md** (Comprehensive Guide)
- **Purpose:** Complete documentation and reference
- **Contains:**
  - Detailed feature explanations
  - Folder structure requirements
  - Command-line options
  - Multi-language support guide
  - Workflow examples
  - Troubleshooting section
  - Integration guide

#### 4. **PROJECT_PROCESSOR_CONFIG.py** (Configuration & Setup)
- **Purpose:** Setup instructions and advanced configuration
- **Contains:**
  - Installation guide
  - Environment variable setup
  - Configuration options
  - Security considerations
  - Performance optimization tips
  - Troubleshooting guide

#### 5. **PROJECT_PROCESSOR_EXAMPLES.py** (Usage Examples)
- **Purpose:** Practical examples of different workflows
- **Contains 10 Examples:**
  1. Basic context generation
  2. Automatic markdown with OpenAI
  3. Batch processing multiple projects
  4. Spanish report handling
  5. Manual LLM processing
  6. Custom processing script
  7. Folder structure best practices
  8. Troubleshooting & tips
  9. CI/CD pipeline integration
  10. Output file reference
- **Includes:** Code snippets and batch scripts

### Reference Files

#### 6. **EXAMPLE_PROJECT_REPORT.txt**
- **Purpose:** Sample project report in the expected format
- **Contains:** A realistic IoT monitoring system project report
- **Use:** Reference for what a report should look like

### Getting Started

**Choose your path:**

```
New to this system?
  └─→ Read: PROJECT_PROCESSOR_QUICKSTART.md (2 min)
      └─→ Run your first project
          └─→ Read: PROJECT_PROCESSOR_README.md (if questions)

Need detailed setup?
  └─→ Read: PROJECT_PROCESSOR_CONFIG.py
      └─→ Run installation commands
          └─→ Try examples from PROJECT_PROCESSOR_EXAMPLES.py

Want to customize?
  └─→ Read: PROJECT_PROCESSOR_README.md (features)
      └─→ Check: PROJECT_PROCESSOR_CONFIG.py (configuration)
          └─→ Modify: project_processor.py

Interested in workflows?
  └─→ Read: PROJECT_PROCESSOR_EXAMPLES.py (all examples)
      └─→ Try specific workflow
          └─→ Adapt to your needs
```

---

## 🚀 Quick Start (60 seconds)

### 1. Prepare Your Project

Create a folder with:
```
my-project/
├── report.txt         ← Project description
├── images/            ← Photos (JPG, PNG)
├── models/            ← 3D models (GLTF, STL)
└── schematics/        ← Diagrams (SVG, PDF)
```

### 2. Run the Processor

```bash
cd scripts
python project_processor.py "path/to/my-project"
```

### 3. Choose Your Path

**Option A - Manual (Free):**
- Copy `llm_prompt.txt` content
- Paste into ChatGPT/Claude
- Copy response as your markdown

**Option B - Automated (Needs OpenAI API):**
```bash
python project_processor.py "path/to/my-project" \
  --output "project.md" \
  --api_key "sk-..." \
  --use-llm
```

### 4. Use Your Markdown

Move files to correct locations:
- Markdown → `_projects/`
- Images → `assets/images/projects/`
- Models → `assets/models/projects/`
- Schematics → `assets/schematics/projects/`

---

## 📋 Feature Checklist

- ✅ Scans project folders for media files
- ✅ Reads project reports (English or Spanish)
- ✅ Auto-detects report language
- ✅ Generates LLM prompts automatically
- ✅ Optional OpenAI API integration
- ✅ Creates context JSON for structured data
- ✅ Supports multiple file formats
- ✅ Works with any LLM (ChatGPT, Claude, Gemini, etc.)
- ✅ Command-line interface with options
- ✅ Error handling and validation
- ✅ Batch processing capability
- ✅ CI/CD ready (GitHub Actions, GitLab CI)

---

## 🎯 Supported Formats

### Media Files

**Images:** JPG, PNG, GIF, WebP, BMP
**3D Models:** GLTF, GLB, STL, OBJ, STEP, STP
**Schematics:** SVG, PDF, PNG, JPG
**Videos:** MP4, WebM, MOV, AVI, MKV
**Reports:** TXT, MD, PDF, DOCX

---

## 📁 System Architecture

```
project_processor.py (Main Script)
├── ProjectScanner (File Discovery)
│   ├── Media file categorization
│   ├── Report reading
│   └── Language detection
├── LLMContextGenerator (Prompt Creation)
│   ├── Prompt formatting
│   ├── JSON context generation
│   └── File reference formatting
└── ProjectProcessor (Orchestration)
    ├── Scanning coordination
    ├── Optional LLM interaction
    └── Output generation
```

---

## 🔄 Typical Workflows

### Workflow 1: Manual (No API)
```
Project Folder → Processor → LLM Prompt → ChatGPT → Markdown
```

### Workflow 2: Automated (API)
```
Project Folder → Processor → OpenAI API → Markdown
```

### Workflow 3: Batch (Multiple Projects)
```
Projects/ → Batch Script → Multiple Markdowns
```

### Workflow 4: CI/CD (GitHub Actions)
```
Push Projects → GitHub Actions → Auto-Process → Site Rebuild
```

---

## 🎓 Learning Path

1. **Beginner:** 
   - Read QUICKSTART
   - Run first project
   - Review generated files

2. **Intermediate:**
   - Read full README
   - Try different options
   - Customize output

3. **Advanced:**
   - Study PROJECT_PROCESSOR_CONFIG.py
   - Implement custom processing
   - Set up CI/CD pipeline

---

## 📞 Help & Support

| Need | Resource |
|------|----------|
| Quick answer | QUICKSTART |
| Detailed info | README |
| Setup help | CONFIG |
| Code examples | EXAMPLES |
| Sample data | EXAMPLE_PROJECT_REPORT.txt |
| Command help | `python project_processor.py --help` |

---

## ✨ Key Benefits

✅ **Automated** - Convert projects to markdown automatically
✅ **Flexible** - Works with any LLM or manually
✅ **Multi-lingual** - Supports English and Spanish reports
✅ **Comprehensive** - Handles images, 3D models, schematics
✅ **Template-aware** - Creates MESGRO-compliant output
✅ **Free** (mostly) - Manual workflow needs no API key
✅ **Scalable** - Process single or multiple projects
✅ **Documented** - Extensive documentation included

---

## 🚀 Next Steps

1. **Read:** `PROJECT_PROCESSOR_QUICKSTART.md` (2 minutes)
2. **Create:** Your first project folder with report and media
3. **Run:** `python project_processor.py "your-project"`
4. **Review:** Generated files (context.json, prompt.txt)
5. **Generate:** Markdown (manually or with API)
6. **Deploy:** Move files to MESGRO structure
7. **Customize:** Adjust markdown as needed
8. **Publish:** Commit and push to GitHub

---

**Last Updated:** December 2024
**Version:** 1.0
**Status:** Ready for use

---

*For more information, start with PROJECT_PROCESSOR_QUICKSTART.md*
