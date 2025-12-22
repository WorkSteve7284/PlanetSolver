cmake_minimum_required(VERSION 3.30)
project(PlanetSolver LANGUAGES CXX)

# Require support for C++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Allow clangd to be nice
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Add include directory
include_directories("${CMAKE_SOURCE_DIR}")

# Add pybind11
add_subdirectory("${CMAKE_SOURCE_DIR}/../extern/pybind11" "${CMAKE_SOURCE_DIR}/build/pybind11")

# Add source files
set(SOURCES
    pybind.cpp
    src/Galaxy.cpp
    src/Path.cpp
    src/Vector.cpp
    Algorithms/AStar.cpp
    Algorithms/Valid.cpp
)

# Add pybind
pybind11_add_module(planetsolver ${SOURCES})

# Add compile flags
target_compile_options(planetsolver PRIVATE -Wall -O3)