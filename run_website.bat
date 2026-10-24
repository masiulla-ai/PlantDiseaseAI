@echo off
title PlantDiseaseAI Web Server
echo ===================================================
echo     Starting PlantDiseaseAI Web Application
echo ===================================================
echo.
cd /d "%~dp0"
if exist .\.venv\Scripts\activate.bat (
    call .\.venv\Scripts\activate.bat
)
echo Starting FastAPI web server at http://localhost:8000 ...
echo Opening your default browser...
start http://localhost:8000
python server.py
pause
