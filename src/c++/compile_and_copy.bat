cd /d "%~dp0"

cmake -B build -G Ninja

cmake --build build

copy "build\planetsolver_cxx.pyd" "..\python\" /Y