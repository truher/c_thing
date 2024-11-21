cmake_minimum_required (VERSION 3.22)
project (hello)

set(DEV_MODULE Development.Module)
find_package(Python 3.8 COMPONENTS Interpreter ${DEV_MODULE} REQUIRED)
set(CMAKE_BUILD_TYPE Release)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ext/nanobind)

nanobind_add_module(
    hello 
    "Hello/hello.cpp"
    "Hello/Speaker.cpp"
    )