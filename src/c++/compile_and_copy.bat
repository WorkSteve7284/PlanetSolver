@echo off

REM This is a convenience script to easily compile the code, and copy generated files to their locations.

cd /d "%~dp0"

REM Compiling
cmake -B build -G Ninja
cmake --build build

REM Copying
copy "build\planetsolver_cxx.pyd" "..\python\" /Y
copy "build\compile_commands.json" "." /Y