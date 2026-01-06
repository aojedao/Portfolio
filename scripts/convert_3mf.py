#!/usr/bin/env python3
"""
3MF to glTF Converter
Converts 3MF files to glTF/glb format
Requires: trimesh, numpy
"""

import os
import sys
import argparse
from pathlib import Path

def install_requirements():
    """Install required packages"""
    try:
        import trimesh
    except ImportError:
        print("Installing required packages...")
        os.system(f'"{sys.executable}" -m pip install trimesh pyassimp numpy')

def convert_3mf_to_gltf(input_file, output_file=None, binary=True):
    """Convert 3MF file to glTF or glb with colors preserved"""
    try:
        import trimesh
    except ImportError:
        print("Error: trimesh not installed. Installing...")
        os.system(f'"{sys.executable}" -m pip install trimesh')
        import trimesh
    
    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        return False
    
    if output_file is None:
        # Save in the same directory as the input file
        input_dir = os.path.dirname(os.path.abspath(input_file))
        base = Path(input_file).stem
        output_file = os.path.join(input_dir, f"{base}.{'glb' if binary else 'gltf'}")
    else:
        # Ensure output directory exists
        output_dir = os.path.dirname(os.path.abspath(output_file))
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
    
    try:
        print(f"Converting: {input_file}")
        print(f"Output: {output_file}")
        
        # Load the 3MF file
        mesh = trimesh.load(input_file, process=True, maintain_order=True)
        
        # Ensure mesh has vertex colors or materials
        if isinstance(mesh, trimesh.Scene):
            # If it's a scene with multiple meshes, export with all materials
            export_kwargs = {
                'file_type': 'glb' if binary else 'gltf',
                'include_normals': True,
            }
        else:
            # Single mesh - preserve vertex colors if present
            export_kwargs = {
                'file_type': 'glb' if binary else 'gltf',
                'include_normals': True,
            }
        
        # Export as glTF with colors
        mesh.export(output_file, **export_kwargs)
        
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"✓ Success! ({file_size:.2f} MB)\n")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {input_file}: {e}\n")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Convert 3MF files to glTF/glb format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python convert_3mf.py model.3mf
  python convert_3mf.py model.3mf -o output.glb
  python convert_3mf.py -d "folder/with/3mf/files"
  python convert_3mf.py -d "folder" -t  # Save as .gltf (text format)
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
    
    # Install requirements
    install_requirements()
    
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
        print(f"Converting to {'glb (binary)' if binary else 'gltf (text)'}...\n")
        
        successful = 0
        for file in sorted(files):
            if convert_3mf_to_gltf(str(file), binary=binary):
                successful += 1
        
        print(f"\n{'='*50}")
        print(f"Conversion complete: {successful}/{len(files)} successful")
        print(f"Output files in: {args.directory}")
        
    else:
        # Convert single file
        success = convert_3mf_to_gltf(args.input, args.output, binary)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
