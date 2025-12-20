cmake_minimum_required(VERSION 3.30)
project(PlanetSolver LANGUAGES CXX)

# Require support for C++ 20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Allow clangd to be nice
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Add pybind11
include_directories("${CMAKE_SOURCE_DIR}/../extern/pybind11/include")
include_directories("${CMAKE_SOURCE_DIR}")

# Add library
add_library(planetsolver MODULE pybind.cpp)

# Compile to correct format
set_target_properties(planetsolver PROPERTIES PREFIX "" SUFFIX ".pyd")

# Add required Python stuff
find_package(Python COMPONENTS Interpreter Development REQUIRED)
target_include_directories(planetsolver PRIVATE ${Python_INCLUDE_DIRS})
target_link_libraries(planetsolver PRIVATE ${Python_LIBRARIES})

# Add other files

target_sources(planetsolver
    PUBLIC
        src/Vector.cpp
        src/Galaxy.cpp
        src/Path.cpp
        Algorithms/AStar.cpp
        Algorithms/Valid.cpp
)