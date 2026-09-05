@echo off
setlocal
cd /d "%~dp0"

echo ==========================================
echo Titanic Survival Prediction - Launcher
echo ==========================================

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create the virtual environment.
        pause
        exit /b 1
    )
)

echo Installing/verifying dependencies...
venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 (
    echo Dependency installation failed.
    pause
    exit /b 1
)

echo.
echo Starting Streamlit...
venv\Scripts\python.exe -m streamlit run app.py
pause
