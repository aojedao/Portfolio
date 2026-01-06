# Coffee Quality Sensor Project - Image Setup Guide

## Project File Created
✅ **File:** `_projects/coffee-quality-sensor.md`

This is a complete project template for your coffee quality monitoring sensor system.

## Images Needed

The project references these images. Copy them from `C:\Users\USER\Documents\CoffeeHub` to the folder:
`F:\MESGRO\assets\images\projects\coffee-sensor\`

### Required Images (referenced in gallery):

1. **protoboard-setup.jpg**
   - Description: Initial protoboard prototype with ESP32 and distance sensor
   - Expected: Shows the protoboard setup during early development

2. **pcb-design.jpg**
   - Description: PCB design created using Flux AI
   - Expected: Screenshot or schematic of the PCB layout

3. **pcb-prototype.jpg**
   - Description: Manufactured PCB prototype
   - Expected: Photo of the manufactured PCB board

4. **assembly.jpg**
   - Description: Sensor assembly and integration
   - Expected: Photo showing components being assembled

5. **installation.jpg**
   - Description: Installed sensor on coffee drying bed
   - Expected: Photo of sensor in actual deployment

### Featured Image:
- **featured.jpg** - Main project image (used on portfolio grid)

## How to Add Images

### Option 1: Manual Copy (Easiest)
1. Open File Explorer
2. Navigate to: `C:\Users\USER\Documents\CoffeeHub`
3. Copy all images you want to use
4. Paste into: `F:\MESGRO\assets\images\projects\coffee-sensor\`
5. Rename them to match the file names above (if needed)

### Option 2: Using Terminal
```powershell
Copy-Item "C:\Users\USER\Documents\CoffeeHub\*.jpg" `
          "F:\MESGRO\assets\images\projects\coffee-sensor\"
```

## Updating Project Details

The project file includes placeholders for:
- GitHub URL (if you have a repo)
- Demo URL (if hosted online)
- Schematics folder (add later if needed)
- 3D Models (add later if needed)

## Updating Gallery Items

Once images are added, the gallery will automatically display them in the order listed in the YAML frontmatter.

You can add/modify images by editing `_projects/coffee-quality-sensor.md`:

```yaml
gallery:
  - file: "/assets/images/projects/coffee-sensor/your-image.jpg"
    description: "Description of what's shown"
```

## Project Visibility

The project will automatically appear:
- ✅ On the Projects page (`/projects/`)
- ✅ On the home page (if it's in top 9 newest)
- ✅ Full project page at `/projects/coffee-quality-sensor/`

## Next Steps

1. Copy images from CoffeeHub folder to `assets/images/projects/coffee-sensor/`
2. Build and test: `jekyll serve`
3. Verify project displays correctly
4. Add any additional content or schematics if available

## File Locations

```
Project File:     F:\MESGRO\_projects\coffee-quality-sensor.md
Image Folder:     F:\MESGRO\assets\images\projects\coffee-sensor\
Featured Image:   featured.jpg (recommended 800x600px)
Gallery Images:   protoboard-setup.jpg, pcb-design.jpg, etc.
```

---

**Note**: This project file is complete and ready to use once images are added. The system will auto-generate the project page and add it to listings.
