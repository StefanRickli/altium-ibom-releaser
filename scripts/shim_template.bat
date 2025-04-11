@echo off
setlocal

set "PROJECT_ROOT=ROOT_PLACEHOLDER"

if not exist "%PROJECT_ROOT%" (
    echo ❌ Project root not found: %PROJECT_ROOT%
    exit /b 1
)

set "PYTHON_EXEC=%PROJECT_ROOT%\.venv\Scripts\python.exe"

if not exist "%PYTHON_EXEC%" (
    echo ❌ Python not found: %PYTHON_EXEC%
    exit /b 1
)

"%PYTHON_EXEC%" -m altium_ibom_releaser %*
