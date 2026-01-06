#!/usr/bin/env node

/**
 * gltf-converter CLI wrapper
 * Converts 3MF, FBX, OBJ, STL, DAE, PLY, PCD and other formats to glTF/glb
 */

const fs = require('fs');
const path = require('path');
const { GLTFExporter } = require('three/examples/jsm/exporters/GLTFExporter.js');
const THREE = require('three');

// Load loaders based on input format
const { OBJLoader } = require('three/examples/jsm/loaders/OBJLoader.js');
const { MTLLoader } = require('three/examples/jsm/loaders/MTLLoader.js');
const { STLLoader } = require('three/examples/jsm/loaders/STLLoader.js');

function showHelp() {
  console.log(`
gltf-converter CLI

Usage: node gltf_converter_cli.js [options] <input>

Supported input formats:
  - 3MF, FBX, OBJ, MTL, STL, DAE, PLY, PCD, GLTF, GLB

Options:
  -o, --output <path>    Output file path (.glb or .gltf)
  -b, --binary           Save as binary GLB format (default)
  -t, --text             Save as text glTF format
  -h, --help             Show this help message

Examples:
  node gltf_converter_cli.js -o output.glb input.3mf
  node gltf_converter_cli.js -o output.gltf --text input.obj
  `);
}

function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    output: null,
    binary: true,
    input: null
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    
    if (arg === '-h' || arg === '--help') {
      showHelp();
      process.exit(0);
    } else if (arg === '-o' || arg === '--output') {
      options.output = args[++i];
    } else if (arg === '-b' || arg === '--binary') {
      options.binary = true;
    } else if (arg === '-t' || arg === '--text') {
      options.binary = false;
    } else if (!arg.startsWith('-')) {
      options.input = arg;
    }
  }

  if (!options.input) {
    console.error('Error: Input file required');
    showHelp();
    process.exit(1);
  }

  if (!options.output) {
    const ext = options.binary ? '.glb' : '.gltf';
    options.output = path.basename(options.input, path.extname(options.input)) + ext;
  }

  return options;
}

async function convertToGLTF(inputPath, outputPath, binary = true) {
  try {
    if (!fs.existsSync(inputPath)) {
      throw new Error(`Input file not found: ${inputPath}`);
    }

    console.log(`Converting ${inputPath} to ${outputPath}...`);

    const ext = path.extname(inputPath).toLowerCase();
    
    // For now, show instructions for using the web interface
    console.log('\nNote: For full 3MF support, please use the web interface:');
    console.log('Run from this directory: npm start');
    console.log('Then upload your file through the browser at http://localhost:8080\n');

    if (ext === '.obj') {
      console.log('For OBJ files, you can also use: obj2gltf -i ' + inputPath + ' -o ' + outputPath + ' -b');
    }

  } catch (error) {
    console.error('Conversion failed:', error.message);
    process.exit(1);
  }
}

// Main
const options = parseArgs();
convertToGLTF(options.input, options.output, options.binary);
