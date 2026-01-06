#!/usr/bin/env python3
"""
3MF to glTF Converter using Blender
Converts 3MF files to glTF/glb format with proper color preservation
Requires: Blender 3.0+
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def find_blender():
    """Find Blender executable"""
    possible_paths = [
        r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.6\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 3.5\blender.exe",
    ]
    
    # Try to find any Blender installation
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # Try to find in Program Files
    base_path = r"C:\Program Files\Blender Foundation"
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            blender_exe = os.path.join(base_path, folder, "blender.exe")
            if os.path.exists(blender_exe):
                return blender_exe
    
    return None

def create_blender_script(input_file, output_file):
    """Create a Blender Python script for conversion"""
    # Escape backslashes for Blender script
    input_file_escaped = input_file.replace('\\', '\\\\')
    output_file_escaped = output_file.replace('\\', '\\\\')
    
    script = f'''
import bpy
import os

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Import the 3MF file
bpy.ops.import_mesh.threemf(filepath=r'{input_file_escaped}')

# Select all objects
bpy.ops.object.select_all(action='SELECT')

# Export as glTF 2.0
bpy.ops.export_scene.gltf(
    filepath=r'{output_file_escaped}',
    export_format='GLB',
    export_colors=True,
    export_materials=True,
    export_attributes=True,
    use_draco_mesh_compression=False,
    will_save_settings=False
)

print("Conversion complete")
'''
    return script

def convert_3mf_with_blender(input_file, output_file=None, binary=True):
    """Convert 3MF file using Blender"""
    
    blender_exe = find_blender()
    if not blender_exe:
        print("Error: Blender not found. Install Blender 3.0+ from https://www.blender.org")
        return False
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return False
    
    if output_file is None:
        # Save to MESGRO assets/models folder by default
        mesgro_path = r"C:\Users\Alejandro\Documents\Documents\MESGRO\assets\models\advancedmechatronics"
        os.makedirs(mesgro_path, exist_ok=True)
        base = Path(input_file).stem
        output_file = os.path.join(mesgro_path, f"{base}.{'glb' if binary else 'gltf'}")
    else:
        output_dir = os.path.dirname(os.path.abspath(output_file))
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
    
    try:
        print(f"Converting: {input_file}")
        print(f"Output: {output_file}")
        
        # Create temporary Python script
        script_path = os.path.join(os.path.dirname(input_file), "temp_convert.py")
        script_content = create_blender_script(input_file, output_file)
        
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Run Blender in background mode
        cmd = [
            blender_exe,
            "--background",
            "--python", script_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        # Clean up
        if os.path.exists(script_path):
            os.remove(script_path)
        
        if result.returncode == 0 and os.path.exists(output_file):
            file_size = os.path.getsize(output_file) / (1024 * 1024)
            print(f"✓ Success! ({file_size:.2f} MB)\n")
            return True
        else:
            print(f"✗ Blender error:\n{result.stderr}\n")
            return False
        
    except Exception as e:
        print(f"✗ Error converting {input_file}: {e}\n")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Convert 3MF files to glTF/glb format with colors (using Blender)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_3mf_blender.py model.3mf
  python convert_3mf_blender.py model.3mf -o output.glb
  python convert_3mf_blender.py -d "folder/with/3mf/files"
  python convert_3mf_blender.py -d "folder" -t  # Save as .gltf (text format)
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input 3MF file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-d', '--directory', help='Convert all 3MF files in directory')
    parser.add_argument('-t', '--text', action='store_true', help='Save as text glTF (.gltf) instead of binary (.glb)')
    parser.add_argument('--no-binary', action='store_true', help='Alias for --text')
    
    args = parser.parse_args()
    
    if not args.input and not args.directory:
        parser.print_help()
        sys.exit(1)
    
    blender_exe = find_blender()
    if not blender_exe:
        print("\n" + "="*60)
        print("Blender not found!")
        print("Installing Blender now...")
        print("="*60 + "\n")
        os.system("winget install BlenderFoundation.Blender")
        print("\nPlease restart this script after Blender installation completes.")
        sys.exit(1)
    
    print(f"Using Blender: {blender_exe}\n")
    
    binary = not (args.text or args.no_binary)
    
    if args.directory:
        # Batch convert all 3MF files in directory
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {args.directory}")
            sys.exit(1)
        
        files = list(dir_path.glob('*.3mf'))
        if not files:
            print(f"No 3MF files found in {args.directory}")
            sys.exit(0)
        
        print(f"Found {len(files)} 3MF file(s)")
        print(f"Converting to {'glb (binary)' if binary else 'gltf (text)'} with colors...\n")
        
        successful = 0
        for file in sorted(files):
            if convert_3mf_with_blender(str(file), binary=binary):
                successful += 1
        
        print("="*50)
        print(f"Conversion complete: {successful}/{len(files)} successful")
        print(f"Output files in: {args.directory}")
        
    else:
        # Convert single file
        success = convert_3mf_with_blender(args.input, args.output, binary)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
