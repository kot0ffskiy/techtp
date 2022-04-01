cmake_minimum_required(VERSION 3.0)

if(ARM_BUILD)
    set(CMAKE_SYSTEM_PROCESSOR aarch64)
    set(CMAKE_C_COMPILER ${TOOLCHAIN}/aarch64-linux-gnu-gcc)
    set(CMAKE_CXX_COMPILER ${TOOLCHAIN}/aarch64-linux-gnu-g++)
endif()

project(SimpleLibrary)

include_directories(include)

add_subdirectory(src)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)

option(TOOLCHAIN DEFAULT)

add_executable(MainLib main_lib.cpp)
add_executable(Main main.cpp)

target_link_libraries(MainLib buffer)
install(TARGETS Main RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
install(TARGETS MainLib PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
