# Get Python minor version
$pythonVersion = & python --version 2>&1
$pythonMinorVersion = [int]($pythonVersion -split '\.')[1]

if ($pythonMinorVersion -gt 12) {
    Write-Host "Python version 3.$pythonMinorVersion detected. Python 3.12 or lower is required for setup to complete."
    Write-Host "If you have multiple versions of Python installed, you can set the correct one by adjusting setup.ps1 to use a specific version, for example:"
    Write-Host "'python -m venv .venv' -> 'py -3.12 -m venv .venv'"
    exit 1
}

# Check if cargo is installed
if (-not (Get-Command cargo -ErrorAction SilentlyContinue)) {
    Write-Host "Cargo (the package manager for Rust) is not present. This is required for one of this module's dependencies."
    Write-Host "See https://www.rust-lang.org/tools/install for installation instructions."
    exit 1
}

# Create and activate virtual environment
python -m venv .venv
& .\.venv\Scripts\Activate.ps1

# Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r dev-requirements.txt
pre-commit install
