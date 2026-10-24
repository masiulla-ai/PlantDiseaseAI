@echo off
title PlantDiseaseAI Instant Public Tunnel
echo ===================================================
echo   Launching Instant Public Link for PlantDiseaseAI
echo ===================================================
echo.
cd /d "%~dp0"
echo Starting Cloudflare Tunnel for your local website...
echo Note: Keep your server running in the background.
echo.
.\cloudflared.exe tunnel --url http://127.0.0.1:8000
pause
