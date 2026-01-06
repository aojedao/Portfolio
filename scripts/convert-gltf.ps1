# gltf-converter wrapper for mesgro
# Usage: .\convert-gltf.ps1 -Input "file.3mf" -Output "file.glb"

param(
    [Parameter(Mandatory=$true)]
    [string]$Input,
    
    [Parameter(Mandatory=$false)]
    [string]$Output = $null,
    
    [Parameter(Mandatory=$false)]
    [switch]$Text = $false
)

$converterPath = "$env:APPDATA\npm\node_modules\gltf-converter"

if (-not (Test-Path $converterPath)) {
    Write-Error "gltf-converter not found. Please run: npm install -g looeee/gltf-converter"
    exit 1
}

if (-not (Test-Path $Input)) {
    Write-Error "Input file not found: $Input"
    exit 1
}

if ($null -eq $Output) {
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($Input)
    $Output = if ($Text) { "$baseName.gltf" } else { "$baseName.glb" }
}

Write-Host "gltf-converter - Web Interface" -ForegroundColor Green
Write-Host "`nTo convert your file: $Input"
Write-Host "Output will be saved as: $Output`n"

Write-Host "Starting web server..." -ForegroundColor Cyan
Write-Host "Open your browser to: http://localhost:8080" -ForegroundColor Yellow
Write-Host "Upload your file through the web interface.`n"

# Navigate to the converter directory and start the server
Push-Location $converterPath
try {
    npm start
}
finally {
    Pop-Location
}
