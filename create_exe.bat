@echo off
REM Script pour créer l'exe avec PyInstaller

pyinstaller ^
    --onefile ^
    --windowed ^
    --name "Renommeur de Photos" ^
    --path src ^
    --icon=src/assets/icone.ico ^
    --add-data "src/assets/ico.png;assets" ^
    src\photo_renommer\main.py

pause