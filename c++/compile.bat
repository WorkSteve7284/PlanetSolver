@echo OFF

cmake -G Ninja -B build

cmake --build build

copy build\compile_commands.json .

copy build\planetsolver.pyd ..\python