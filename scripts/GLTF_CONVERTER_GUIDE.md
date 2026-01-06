# GLTF Converter Setup Guide

## Installed Tools

### 1. **obj2gltf** (OBJ to GLTF/GLB Converter)
- **Supports**: OBJ + MTL files
- **Installation**: Global npm package
- **Command**: `obj2gltf`
- **Usage**: `obj2gltf -i input.obj -o output.glb -b`

#### Examples:
```powershell
# Basic conversion to GLB
obj2gltf -i model.obj -o model.glb -b

# Keep separate textures
obj2gltf -i model.obj -o model.gltf -s

# With texture overrides
obj2gltf -i model.obj -o model.glb -b --baseColorTexture texture.png
```

### 2. **gltf-converter** (Multi-format Converter)
- **Supports**: 3MF, FBX, OBJ, STL, DAE, PLY, PCD, GLTF, GLB
- **Type**: Web-based converter using three.js
- **Installation**: From GitHub (looeee/gltf-converter)

#### How to Use for 3MF Files:

The gltf-converter is a web interface tool. To convert your 3MF files:

1. **Navigate to the converter directory**:
   ```powershell
   cd $env:APPDATA\npm\node_modules\gltf-converter
   ```

2. **Install dependencies** (first time only):
   ```powershell
   npm install
   ```

3. **Start the web server**:
   ```powershell
   npm start
   ```

4. **Open browser**: Go to `http://localhost:8080`

5. **Upload and convert**:
   - Select your 3MF file(s)
   - Upload any textures (PNG, JPG, etc.) at the same time
   - Choose export format (GLB or GLTF)
   - Download the converted file

#### Supported Formats:
- **Input**: 3MF, AMF, FBX, OBJ+MTL, GLTF, GLB, DAE, PCD, PLY, STL
- **Output**: glTF 2.0 (JSON) or GLB (binary)

#### Notes:
- All conversions happen locally (no data sent to servers)
- Textures should be uploaded together with the model
- MeshStandardMaterial is used for all exports
- Some formats are more limited than others

## Quick Workflow for Your Project

### For OBJ+MTL files (Use obj2gltf):
```powershell
obj2gltf -i "path/to/model.obj" -o "output/model.glb" -b
```

### For 3MF files (Use gltf-converter web interface):
1. Start the web server
2. Upload your 3MF file
3. Download the GLB file
4. Move to your assets folder

## Environment Setup

Your mesgro environment includes:
- Python 3.12.10
- Node.js v24.12.0
- npm 11.6.2

All converter tools are installed globally and available from any terminal.

## Batch Conversion Script

For converting multiple 3MF files, you can create a batch process:
1. Use the web interface to convert each file
2. Or write a Node.js script using the three.js loaders

Example files created:
- `gltf_converter_cli.js` - Node.js CLI wrapper (in progress)
- `convert-gltf.ps1` - PowerShell launcher script

## Troubleshooting

**obj2gltf not found**:
- Refresh PATH: `$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")`

**gltf-converter npm start fails**:
- Run `npm install` in the converter directory first
- Make sure Node.js is properly installed

**Texture not showing**:
- Upload textures with the same directory structure as the original model
- Ensure texture paths in the model file are relative

## Additional Resources

- obj2gltf: https://github.com/CesiumGS/obj2gltf
- gltf-converter: https://github.com/looeee/gltf-converter
- three.js documentation: https://threejs.org/
