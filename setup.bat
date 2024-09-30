@echo off

:: Save the current directory
set ORIGINAL_DIR=%CD%

:: Change to the directory where the script is located
cd /d %~dp0

:: Check if Python is installed
python --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not found in the PATH.
    echo Please install Python from https://www.python.org.
    pause
    exit /b 1
) else (
    echo Python is already installed.
)

:: Install the dependencies globally
echo Installing dependencies globally...
pip install --no-index --find-links=libs/ -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Failed to install dependencies. Please check the requirements.txt file.
    pause
    exit /b 1
)

:: Ensure the directory contains main.py
if not exist "main.py" (
    echo main.py does not exist in the current directory.
    pause
    exit /b 1
)

:: Run Streamlit application
echo Starting Streamlit application...
start "" cmd /k "streamlit run main.py"

:: Return to the original directory
cd /d %ORIGINAL_DIR%

pause
