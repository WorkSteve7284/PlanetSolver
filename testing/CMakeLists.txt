cmake_minimum_required(VERSION 3.14)
project(PlanetSolver LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories("${CMAKE_SOURCE_DIR}/../extern/pybind11/include")

add_library(example MODULE add.cpp)

set_target_properties(example PROPERTIES PREFIX "" SUFFIX ".pyd")

find_package(Python COMPONENTS Interpreter Development REQUIRED)
target_include_directories(example PRIVATE ${Python_INCLUDE_DIRS})
target_link_libraries(example PRIVATE ${Python_LIBRARIES})