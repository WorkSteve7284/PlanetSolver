@echo OFF

cmake -G Ninja -B build -DCMAKE_BUILD_TYPE=Release

cmake --build build

copy build\compile_commands.json .

copy build\planetsolver.pyd ..\python