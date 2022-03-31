add_library(buffer SHARED buffer.cpp)
install(TARGETS buffer PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)