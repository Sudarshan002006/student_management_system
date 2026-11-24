@echo off
title MANBHUM VICTORIA INSTITUTION - Grade Management System
echo.
echo ============================================
echo  MANBHUM VICTORIA INSTITUTION
echo  Student Grade Management System
echo ============================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Install Flask if needed
echo [1/3] Checking Flask installation...
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo Installing Flask...
    pip install Flask>=3.0
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Flask.
        pause
        exit /b 1
    )
)

:: Start the Flask server in background
echo [2/3] Starting server on http://127.0.0.1:5000 ...
start "" python app.py

:: Wait a moment for server to start
timeout /t 3 >nul

:: Open the website in default browser
echo [3/3] Opening website in browser...
start "" http://127.0.0.1:5000

echo.
echo ============================================
echo  Website is now running!
echo  Local URL:  http://127.0.0.1:5000
echo  Network URL: http://10.183.219.135:5000
echo ============================================
echo.
echo Press any key to close this window (keeps server running).
pause >nul
