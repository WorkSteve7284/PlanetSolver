cmake_minimum_required(VERSION 3.30)
project(PlanetSolver LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include_directories("${CMAKE_SOURCE_DIR}/../../extern/pybind11/include")

add_library(planetsolver_cxx MODULE pybind.cpp)

set_target_properties(planetsolver_cxx PROPERTIES PREFIX "" SUFFIX ".pyd")

find_package(Python COMPONENTS Interpreter Development REQUIRED)
target_include_directories(planetsolver_cxx PRIVATE ${Python_INCLUDE_DIRS})
target_link_libraries(planetsolver_cxx PRIVATE ${Python_LIBRARIES})