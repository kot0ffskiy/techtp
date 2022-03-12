cmake_minimum_required(VERSION 3.0)

project(task2)

execute_process(
    COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/A
)

set(SOURCE_EXE ${PROJECT_SOURCE_DIR}/C/main.cpp)

include_directories(${PROJECT_SOURCE_DIR})

add_subdirectory(${PROJECT_SOURCE_DIR}/B ${PROJECT_SOURCE_DIR}/lib)

add_executable(C ${SOURCE_EXE})

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

target_link_libraries(C lib)