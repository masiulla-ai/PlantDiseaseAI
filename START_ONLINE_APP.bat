@echo off
title Plant Disease AI - Master Launcher
echo ============================================================
echo        Plant Disease AI - Launcher (Independent of IDE)
echo ============================================================
echo.
cd /d "%~dp0"

echo [1/3] Checking dependencies...
if not exist ".\.venv\Scripts\python.exe" (
    echo Error: Python virtual environment not found in %~dp0.venv
    pause
    exit /b 1
)

echo [2/3] Starting AI Backend Server...
start "PlantDiseaseAI - Server" /min cmd /k "cd /d "%~dp0" && .\.venv\Scripts\python.exe server.py"

echo Waiting 8 seconds for Deep Learning model to warm up...
timeout /t 8 /nobreak >nul

echo [3/3] Opening local website and starting Cloudflare Public Tunnel...
start http://localhost:8000

echo.
echo ============================================================
echo  YOUR SITE IS NOW RUNNING!
echo  Look below for your generated trycloudflare.com link.
echo.
echo  * You can CLOSE Antigravity!
echo  * Just keep this black command window open to stay online.
echo ============================================================
echo.
.\cloudflared.exe tunnel --url http://127.0.0.1:8000
pause
