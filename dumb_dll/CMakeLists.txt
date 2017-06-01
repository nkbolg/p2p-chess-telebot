cmake_minimum_required(VERSION 2.8.9)


project(DumbDLL)

set(sources DumbDLL.cpp)

add_definitions(-DDUMBDLL_EXPORTS)

add_library(DumbDLL SHARED ${sources})
