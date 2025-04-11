
$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "Continue"

# Try getting python directly
$systemPythonPath = & python -c "import sys; print(sys.executable)" 2>$null
if (-not $systemPythonPath) {
    # Fallback: try with py launcher
    $systemPythonPath = & py -c "import sys; print(sys.executable)" 2>$null
}

$ErrorActionPreference = $previousErrorActionPreference

if (-not $systemPythonPath) {
    throw "Python executable not found"
}

# Output the path
Write-Output $systemPythonPath
