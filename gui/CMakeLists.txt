cmake_minimum_required(VERSION 3.19)
project(CryptKey LANGUAGES CXX)

# Find Qt6 (if you need Qt features; if you’re building a CLI-only backend, you can remove these lines)
find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets)
qt_standard_project_setup()

# Create the executable target using sources from the src folder.
# We remove the mainwindow files to use only CLI logic from main.cpp.
qt_add_executable(CryptKey
    WIN32 MACOSX_BUNDLE
    ../src/main.cpp
    ../src/FileHandler.cpp
    ../src/PasswordGenerator.cpp
)

# Specify include directories so that the headers in crypt-key/include are found.
target_include_directories(CryptKey
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/../include
)

# Link against Qt libraries if needed (remove these if building pure CLI):
target_link_libraries(CryptKey
    PRIVATE
        Qt6::Core
        Qt6::Widgets
)

include(GNUInstallDirs)

install(TARGETS CryptKey
    BUNDLE DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

qt_generate_deploy_app_script(
    TARGET CryptKey
    OUTPUT_SCRIPT deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)
install(SCRIPT ${deploy_script})