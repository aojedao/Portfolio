# Coffee Quality Sensor - Add Images

The Coffee Quality Sensor project has been created WITHOUT images (since I can't directly copy from your external folder).

## To Add Images:

### Option 1: Copy images from your folder
```powershell
# Open PowerShell and run:
Copy-Item "C:\Users\USER\Documents\CoffeeHub\*.jpg" `
          "F:\MESGRO\assets\images\projects\coffee-sensor\" -Force
```

### Option 2: Manual copy
1. Open File Explorer
2. Go to: `C:\Users\USER\Documents\CoffeeHub\`
3. Select the images you want
4. Copy them
5. Paste to: `F:\MESGRO\assets\images\projects\coffee-sensor\`

### Option 3: Add images one at a time
1. Choose an image from CoffeeHub
2. Copy to: `F:\MESGRO\assets\images\projects\coffee-sensor\`
3. Edit the project file to add it to the gallery

## To Add Gallery Items

After copying images, edit `_projects/coffee-quality-sensor.md` and update the gallery section:

```yaml
gallery:
  - file: "/assets/images/projects/coffee-sensor/protoboard-setup.jpg"
    description: "Initial protoboard prototype with ESP32 and distance sensor"
  - file: "/assets/images/projects/coffee-sensor/pcb-design.jpg"
    description: "PCB design created using Flux AI"
  - file: "/assets/images/projects/coffee-sensor/pcb-prototype.jpg"
    description: "Manufactured PCB prototype"
  - file: "/assets/images/projects/coffee-sensor/assembly.jpg"
    description: "Sensor assembly and integration"
  - file: "/assets/images/projects/coffee-sensor/installation.jpg"
    description: "Installed sensor on coffee drying bed"
```

## Current Status

✅ Project file created: `_projects/coffee-quality-sensor.md`  
✅ Image folder created: `assets/images/projects/coffee-sensor/`  
❌ Images: Not copied (awaiting your action)  

The project displays fine without images but will look better once you add them.

## Image Folder Location
```
F:\MESGRO\assets\images\projects\coffee-sensor\
```

This is where the images need to go.
