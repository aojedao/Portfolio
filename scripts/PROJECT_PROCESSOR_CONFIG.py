"""
MESGRO Project Processor Configuration & Setup Guide

This file provides setup instructions and configuration options for the
Project Processor system.
"""

# ==============================================================================
# INSTALLATION GUIDE
# ==============================================================================

"""
STEP 1: Verify Python Installation
====================================

Windows:
    python --version

Should output Python 3.8 or higher

STEP 2: Install Optional Dependencies
======================================

For OpenAI LLM Integration:
    pip install openai

For PDF Report Reading:
    pip install pdfplumber

For DOCX Report Reading:
    pip install python-docx

For All Features:
    pip install openai pdfplumber python-docx

STEP 3: Get OpenAI API Key (Optional)
======================================

1. Go to https://platform.openai.com/api-keys
2. Sign in with your OpenAI account
3. Create a new API key
4. Copy and save it securely
5. Use with --api_key flag when running processor

STEP 4: Test Installation
===========================

cd scripts
python project_processor.py --help

Should show help message with all options
"""


# ==============================================================================
# ENVIRONMENT VARIABLES (Optional)
# ==============================================================================

"""
Instead of --api_key on command line, you can set environment variable:

Windows PowerShell:
    $env:OPENAI_API_KEY = "sk-your-key-here"
    python project_processor.py "project" --use-llm

Windows Command Prompt:
    set OPENAI_API_KEY=sk-your-key-here
    python project_processor.py "project" --use-llm

Linux/Mac:
    export OPENAI_API_KEY="sk-your-key-here"
    python project_processor.py "project" --use-llm

This keeps your API key out of command history.
"""


# ==============================================================================
# CONFIGURATION OPTIONS
# ==============================================================================

class ProcessorConfig:
    """
    Configuration settings for the Project Processor
    Modify these to customize behavior
    """
    
    # File Extensions
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff'}
    MODEL_EXTENSIONS = {'.gltf', '.glb', '.stl', '.obj', '.step', '.stp', '.iges'}
    VIDEO_EXTENSIONS = {'.mp4', '.webm', '.mov', '.avi', '.mkv', '.flv', '.wmv'}
    SCHEMATIC_EXTENSIONS = {'.svg', '.pdf', '.png', '.jpg', '.jpeg'}
    REPORT_EXTENSIONS = {'.txt', '.md', '.pdf', '.docx', '.doc'}
    
    # LLM Settings
    LLM_MODEL = "gpt-4-turbo"  # or "gpt-3.5-turbo" for faster/cheaper
    LLM_TEMPERATURE = 0.7  # 0.0 = deterministic, 1.0 = creative
    LLM_MAX_TOKENS = 4000  # Maximum response length
    LLM_TOP_P = 0.95  # Nucleus sampling parameter
    
    # Processing Options
    RECURSIVE_SCAN = True  # Scan all subdirectories
    SKIP_HIDDEN_FILES = True  # Ignore files starting with .
    MIN_IMAGE_SIZE = 100  # Minimum image dimension in pixels
    
    # Output Options
    GENERATE_CONTEXT_JSON = True
    GENERATE_PROMPT_TXT = True
    VERBOSE_OUTPUT = False
    
    # Logging
    LOG_FILE = "processor.log"
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR


# ==============================================================================
# USAGE WORKFLOWS
# ==============================================================================

"""
WORKFLOW 1: Local Development (No Cloud)
==========================================

1. Create project folder with report and media
2. Run: python project_processor.py "project"
3. Open llm_prompt.txt
4. Paste into ChatGPT/Claude/Gemini
5. Copy response
6. Manually create markdown file
7. Review and adjust
8. Move to _projects/ folder

Pros: Free, no API key needed, full control
Cons: Manual, slower, requires LLM subscription separately


WORKFLOW 2: Automated with API (Recommended for Teams)
========================================================

1. Set up OpenAI API key
2. Create project folder with report and media
3. Run: python project_processor.py "project" --output "out.md" --api_key "sk-..." --use-llm
4. Review generated markdown
5. Make any adjustments needed
6. Move media files to assets/
7. Move markdown to _projects/
8. Commit and push to GitHub

Pros: Fully automated, consistent results, version controlled
Cons: Requires OpenAI API account and credits


WORKFLOW 3: Batch Processing (Multiple Projects)
==================================================

1. Organize all projects in projects/
2. Set OPENAI_API_KEY environment variable
3. Run batch script (see PROJECT_PROCESSOR_EXAMPLES.py)
4. Review all generated markdown files
5. Move assets and markdown to correct locations
6. Single commit with all projects

Pros: Efficient for multiple projects, batch processing
Cons: Requires API key, needs script customization


WORKFLOW 4: CI/CD Integration (GitHub Actions)
================================================

1. Add secrets to GitHub: OPENAI_API_KEY
2. Create .github/workflows/process-projects.yml
3. Configure workflow (see PROJECT_PROCESSOR_EXAMPLES.py)
4. Push projects to projects/ folder
5. GitHub Actions automatically processes them
6. Markdown committed to _projects/
7. GitHub Pages rebuilds site

Pros: Fully automated, always up-to-date, CI/CD
Cons: Requires GitHub and GitHub Actions knowledge
"""


# ==============================================================================
# ADVANCED CONFIGURATION
# ==============================================================================

"""
CUSTOMIZING THE LLM MODEL
===========================

For faster responses (cheaper):
    ProcessorConfig.LLM_MODEL = "gpt-3.5-turbo"
    ProcessorConfig.LLM_MAX_TOKENS = 2000

For better quality (slower, more expensive):
    ProcessorConfig.LLM_MODEL = "gpt-4"
    ProcessorConfig.LLM_MAX_TOKENS = 8000

For creative/varied outputs:
    ProcessorConfig.LLM_TEMPERATURE = 0.9

For consistent/predictable outputs:
    ProcessorConfig.LLM_TEMPERATURE = 0.3


CUSTOMIZING OUTPUT
===================

To skip JSON context generation:
    ProcessorConfig.GENERATE_CONTEXT_JSON = False

To get detailed logs:
    ProcessorConfig.VERBOSE_OUTPUT = True
    ProcessorConfig.LOG_LEVEL = "DEBUG"

To add custom file extensions:
    ProcessorConfig.MODEL_EXTENSIONS.add('.dwg')
    ProcessorConfig.IMAGE_EXTENSIONS.add('.ico')


MODIFYING SUPPORTED FORMATS
=============================

Edit project_processor.py:

# Add support for additional formats
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff', '.ico'}
MODEL_EXTENSIONS = {'.gltf', '.glb', '.stl', '.obj', '.step', '.stp', '.iges', '.dwg'}

Restart the processor after modification.
"""


# ==============================================================================
# SECURITY CONSIDERATIONS
# ==============================================================================

"""
API KEY SECURITY
=================

DO NOT:
    - Put API key in version control (git commit)
    - Share API key in public repositories
    - Hardcode API key in scripts
    - Expose API key in logs

DO:
    - Use environment variables: OPENAI_API_KEY
    - Use --api_key flag only locally
    - Rotate API keys regularly
    - Monitor usage at https://platform.openai.com/usage
    - Set spending limits in OpenAI dashboard

GitHub Secrets Setup:
    1. Go to Settings → Secrets and variables → Actions
    2. Click "New repository secret"
    3. Name: OPENAI_API_KEY
    4. Value: sk-... (your API key)
    5. Click "Add secret"

Then in workflow:
    env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}


DATA PRIVACY
============

The processor:
    - Reads local files from your computer
    - Can send content to OpenAI API (if --use-llm used)
    - Saves generated files locally
    - Does NOT upload to any database automatically

Be aware:
    - OpenAI may use prompts for model training (unless opted out)
    - Check OpenAI's privacy policy
    - Consider sensitive project information before using API
    - For proprietary projects, use manual workflow
"""


# ==============================================================================
# TROUBLESHOOTING & SUPPORT
# ==============================================================================

"""
COMMON ERRORS & FIXES
=======================

Error: "ModuleNotFoundError: No module named 'openai'"
Fix:
    pip install openai

Error: "AuthenticationError: Incorrect API key provided"
Fix:
    1. Verify API key is correct at https://platform.openai.com/api-keys
    2. Ensure key starts with "sk-"
    3. Try with --api_key flag instead of environment variable
    4. Check for extra spaces or quotes

Error: "RateLimitError: Rate limit exceeded"
Fix:
    - Wait a few minutes
    - Upgrade OpenAI plan for higher limits
    - Use cheaper model: gpt-3.5-turbo

Error: "Project path not found"
Fix:
    - Check path is correct and exists
    - Use absolute path instead of relative
    - Check for typos in folder name

Error: "Report not found"
Fix:
    - Name report file as: report.txt, report.md, etc.
    - Place in root of project folder
    - Ensure file extension is recognized


CHECKING OPENAI USAGE
======================

Visit: https://platform.openai.com/usage
View:
    - Current month's spending
    - API requests breakdown
    - Model usage statistics

Set Spending Limit:
    Settings → Billing & usage limits
    Set "Hard limit" to control costs


GETTING HELP
============

1. Check PROJECT_PROCESSOR_README.md for detailed docs
2. Review PROJECT_PROCESSOR_EXAMPLES.py for examples
3. Read PROJECT_PROCESSOR_QUICKSTART.md for quick start
4. Run: python project_processor.py --help
5. Check error messages for specific guidance
6. Review project folder structure against QUICKSTART
"""


# ==============================================================================
# SYSTEM REQUIREMENTS
# ==============================================================================

"""
Minimum Requirements:
    - Python 3.8 or higher
    - 100 MB disk space for scripts and outputs
    - 2 GB RAM for processing
    - Internet connection (if using LLM API)

Recommended:
    - Python 3.10 or higher
    - 1 GB disk space for large projects
    - 4 GB RAM for multiple concurrent processing
    - Stable internet connection

Supported Operating Systems:
    - Windows 10, 11
    - macOS 10.15+
    - Linux (any distribution)

Tested On:
    - Windows 11 with Python 3.10
    - Ubuntu 20.04 with Python 3.9
    - macOS 13 with Python 3.11
"""


# ==============================================================================
# PERFORMANCE TIPS
# ==============================================================================

"""
OPTIMIZING PROCESSING SPEED
=============================

1. Use gpt-3.5-turbo model (faster than GPT-4)
2. Reduce max_tokens if generating shorter markdown
3. Organize files before processing (clear structure)
4. Process projects sequentially, not in parallel
5. Use context-only mode to skip LLM for testing

Example optimized command:
    python project_processor.py "project" \\
        --api_key "sk-..." \\
        --use-llm \\
        --output "fast.md"
    # Uses gpt-3.5-turbo by default (fast)


MANAGING LARGE PROJECTS
========================

For projects with many files:
    1. Process in smaller batches
    2. Use --context-only first to verify files
    3. Optimize large images before processing
    4. Remove unnecessary files from folder

Large File Handling:
    - Image size: <5 MB each
    - Video files: Keep in assets/, reference in markdown
    - Model files: >10 MB may slow processing


BATCH PROCESSING OPTIMIZATION
==============================

For multiple projects:
    1. Create sequential script (see EXAMPLES)
    2. Process during off-peak hours
    3. Monitor API usage and costs
    4. Save context JSON for later use
    5. Parallelize on separate machines if needed
"""


# ==============================================================================
# UPDATES & MAINTENANCE
# ==============================================================================

"""
CHECKING FOR UPDATES
======================

GitHub:
    https://github.com/aojedao/MESGRO/tree/main/scripts

Check if newer version available:
    - Download latest project_processor.py
    - Compare version in file docstring
    - Review CHANGELOG.md for changes

Keeping Your Setup Current:
    1. Periodically check for updates
    2. Update dependencies: pip install --upgrade openai
    3. Monitor Python version for deprecations
    4. Test with new LLM models as available
    5. Review template in _projects/ for changes


CLEANING UP
============

Remove old outputs:
    rm *_context.json
    rm *_prompt.txt

Archive processed projects:
    mkdir archive
    mv project-name/ archive/

Clean pyc files:
    find . -type d -name __pycache__ -exec rm -r {} +
"""

print(__doc__)
