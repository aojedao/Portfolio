# 📌 MESGRO Project Processor - Quick Reference Card

## ⚡ 30-Second Overview

A Python system that:
1. Scans project folders for images, 3D models, and schematics
2. Reads project reports (English or Spanish)
3. Generates LLM prompts automatically
4. Optionally creates markdown using OpenAI API

**Result:** MESGRO-formatted project markdown, ready for GitHub Pages

---

## 🎬 Get Started (3 Steps)

### Step 1: Create Project Folder
```
my-project/
├── report.txt          ← Your project description
├── images/             ← Photos (JPG, PNG)
├── models/             ← 3D files (GLTF, STL)
└── schematics/         ← Diagrams (SVG, PDF)
```

### Step 2: Run Processor
```bash
cd scripts
python project_processor.py "path/to/my-project"
```

### Step 3: Generate Markdown
**Option A - Manual (Free):**
- Copy `llm_prompt.txt`
- Paste into ChatGPT/Claude
- Copy response → `_projects/project.md`

**Option B - Automated:**
```bash
python project_processor.py "path" --output "out.md" --api_key "sk-..." --use-llm
```

---

## 📂 Supported File Types

| Type | Extensions |
|------|-----------|
| **Images** | .jpg .png .gif .webp .bmp |
| **3D Models** | .gltf .glb .stl .obj .step .stp |
| **Schematics** | .svg .pdf .png .jpg |
| **Videos** | .mp4 .webm .mov .avi .mkv |
| **Reports** | .txt .md .pdf .docx |

---

## 💻 Command Cheat Sheet

```bash
# Basic scan
python project_processor.py "folder"

# Generate markdown (manual)
python project_processor.py "folder"
# Then use llm_prompt.txt with ChatGPT

# Generate markdown (automated)
python project_processor.py "folder" \
  --output "project.md" \
  --api_key "sk-xxx" \
  --use-llm

# Help
python project_processor.py --help
```

---

## 📚 Documentation Files

| File | Purpose | Read Time |
|------|---------|-----------|
| **QUICKSTART.md** | Quick reference | 2 min ⭐ |
| **README.md** | Full documentation | 15 min |
| **CONFIG.py** | Setup & config | 10 min |
| **EXAMPLES.py** | Code examples | 10 min |
| **INDEX.md** | Documentation index | 5 min |

**👉 Start with QUICKSTART.md**

---

## 🌍 Language Support

- **English** ✅ Automatic detection
- **Spanish** ✅ Automatic detection & translation
- Other languages → Manual translation recommended

---

## 🔑 API Key Setup (Optional)

### Get Key
1. Go to https://platform.openai.com/api-keys
2. Create new key
3. Copy and save securely

### Use Key
```bash
# Option 1: Command line
python project_processor.py "folder" --api_key "sk-..." --use-llm

# Option 2: Environment variable
export OPENAI_API_KEY="sk-..."
python project_processor.py "folder" --use-llm

# Option 3: Don't use API (manual workflow - free!)
python project_processor.py "folder"
```

---

## 🗂️ File Organization

```
f:\MESGRO\
├── scripts/
│   ├── project_processor.py        ← Main script
│   ├── PROJECT_PROCESSOR_README.md
│   ├── PROJECT_PROCESSOR_QUICKSTART.md
│   ├── PROJECT_PROCESSOR_CONFIG.py
│   ├── PROJECT_PROCESSOR_EXAMPLES.py
│   └── EXAMPLE_PROJECT_REPORT.txt
├── _projects/                      ← Your markdown files go here
├── assets/
│   ├── images/projects/
│   ├── models/projects/
│   └── schematics/projects/
└── DELIVERY_SUMMARY.md             ← Complete delivery info
```

---

## ✅ Verification Checklist

Before running processor, ensure:

- [ ] Python 3.8+ installed
- [ ] Project folder created with required structure
- [ ] Report file named `report.txt` or `report.md`
- [ ] Images in `images/` folder
- [ ] Models in `models/` folder (optional)
- [ ] Schematics in `schematics/` folder (optional)

---

## 🎯 Typical Workflow

```
1. Create project folder
   ↓
2. Add report.txt + media files
   ↓
3. Run: python project_processor.py "project"
   ↓
4. Review: project_context.json, llm_prompt.txt
   ↓
5. Generate markdown:
   - Manual: Copy prompt → ChatGPT → Get markdown
   - Auto: Add --api_key --use-llm → Get markdown
   ↓
6. Move files to MESGRO structure
   ↓
7. Push to GitHub
```

---

## 🚨 Common Issues

| Problem | Solution |
|---------|----------|
| "Project not found" | Check path is correct |
| "Report not found" | Name it `report.txt` in folder root |
| "No files found" | Check file extensions match supported formats |
| "API error" | Verify API key and OpenAI account has credits |

For more: See PROJECT_PROCESSOR_README.md

---

## 📋 Output Files Explained

When you run the processor, it creates:

1. **llm_prompt.txt** - Copy into ChatGPT/Claude for markdown
2. **project_context.json** - Structured data about your project
3. **output.md** (if using --output) - Generated markdown (with API)

---

## 💡 Pro Tips

✨ **Best Practices:**
- Name your featured image `featured.jpg` (256×256 min)
- Use descriptive file names (e.g., `main-circuit.svg`)
- Keep report.txt clear and organized
- Review llm_prompt.txt before sending to LLM
- Test all links in generated markdown

✨ **Performance:**
- Use gpt-3.5-turbo for faster responses (modify CONFIG)
- Process during off-peak hours to avoid rate limits
- Batch similar projects together

✨ **Quality:**
- Always review generated markdown
- Test 3D models render in browser
- Verify all image links work
- Check file paths match your assets folder

---

## 🔗 Key Links

- OpenAI API Keys: https://platform.openai.com/api-keys
- MESGRO Repository: https://github.com/aojedao/MESGRO
- Documentation: See PROJECT_PROCESSOR_README.md

---

## 📞 Need Help?

1. **Quick question?** → Read QUICKSTART.md
2. **How do I...?** → Check PROJECT_PROCESSOR_EXAMPLES.py
3. **Setup issue?** → See PROJECT_PROCESSOR_CONFIG.py
4. **Something broken?** → Review PROJECT_PROCESSOR_README.md

---

## ✨ What You Get

✅ Fully automated project processing
✅ Multi-language support (English/Spanish)
✅ Works with any LLM or your favorite API
✅ Production-ready code with error handling
✅ Comprehensive documentation
✅ 10+ practical examples
✅ Sample data and reference reports
✅ Optional CI/CD integration

---

**Status:** ✅ Ready to Use
**Version:** 1.0
**Created:** December 31, 2024

**👉 Next Step:** Open PROJECT_PROCESSOR_QUICKSTART.md
