# CryptKey - ! WARNING: these are all temporary placeholders, will finalize later ! 

This is project for creating an offline password manager, demonstrating proficiency in C++ programming, GUI development, and software design principles.

**Goal:** Securely store passwords locally on the user's machine without internet connectivity.

## Features

- **Offline Use:** Local password storage and exporting
- **Password Generation:** Generates secure passwords using a mix of characters.
- **Console and GUI Interfaces:** Offers both console-based and graphical user interfaces.
- **Data Storage:** Saves password entries to a CSV file (`user_data.csv`).
- **File Handling:** Checks for existing entries and handles file operations.

## Getting Started

### Prerequisites

- **Operating System:** Windows 11
- **Compiler:** GCC (MinGW-w64) or compatible
- **Development Environment:** Visual Studio Code (VSCode)
- **Dependencies:**
  - [GLFW](https://www.glfw.org/)
  - [GLAD](https://glad.dav1d.de/)
  - [Dear ImGui](https://github.com/ocornut/imgui)
  - [MSYS2](https://www.msys2.org/) for GCC and Unix tools on Windows

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ryu-134/offline-password-manager.git
   ```

2. **Install Dependencies:**

   - **GLFW:**  
     Download and build from [glfw.org](https://www.glfw.org/).  
     Place the compiled libraries in `gui/GLFW/`.

   - **GLAD:**  
     Generate the loader from [glad.dav1d.de](https://glad.dav1d.de/).  
     Place the files in `gui/GLAD/`.

   - **Dear ImGui:**  
     Clone or download from [GitHub](https://github.com/ocornut/imgui).  
     Place the necessary files in `gui/ImGui/`.

3. **Set Up the Directory Structure:**

   Ensure your project directory is organized as follows:

   ```plaintext
   PasswordManager/
   ├── src/
   │   ├── main.cpp
   │   ├── PasswordGenerator.cpp
   │   └── FileHandler.cpp
   ├── include/
   │   ├── PasswordGenerator.h
   │   ├── FileHandler.h
   │   └── gui.h
   ├── gui/
   │   ├── gui.cpp
   │   ├── ImGui/
   │   ├── GLFW/
   │   └── GLAD/
   ├── .vscode/
       ├── tasks.json
       └── launch.json


4. **Configure VSCode:**

   - Place `tasks.json` and `launch.json` in the `.vscode/` directory.
   - Adjust paths in `tasks.json` and `launch.json` to match your directory structure.

### Build the Project

1. Open the project in VSCode.
2. Use the provided `tasks.json` to build the project:
   - Press `Ctrl+Shift+B` and select "Build Entire Project (Powershell)".

### Running the Application

- **GUI Version:**
  - Ensure the GUI code is uncommented in `main.cpp`.
  - Run the application using VSCode's debugger or execute `output.exe` from the `build/` directory.

- **Console Version:**
  - Comment out the GUI code and uncomment the console application code in `main.cpp`.
  - Rebuild the project.
  - Run the application from the terminal or VSCode.

## Usage

### GUI Interface:

1. Launch the application.
2. Enter the site and username in the respective fields.
3. Click "Generate Password" to create a new password.
4. Click "Save Entry" to save the details to `user_data.csv`.

### Console Interface:

1. Run the application in the terminal.
2. Follow the prompts to enter the site and username.
3. The application will generate a password and display it.
4. Confirm if you want to save the entry.

## Project Structure

- `src/`: Contains the source code (.cpp files).
- `include/`: Contains the header files (.h files).
- `gui/`: Contains GUI-related source files and third-party libraries.
- `.vscode/`: Contains VSCode configuration files.
- `build/`: Contains the compiled executable and build artifacts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dear ImGui for the GUI library.
- GLFW for window creation and management.
- GLAD for OpenGL function loading.

---

# Build Environment Setup

## Prerequisites

- **Operating System:** Windows 11
- **Compiler:** GCC (MinGW-w64)
- **IDE:** Visual Studio Code (VSCode)
- **Dependencies:**
  - [GLFW](https://www.glfw.org/)
  - [GLAD](https://glad.dav1d.de/)
  - [Dear ImGui](https://github.com/ocornut/imgui)
- **Tools:**
  - [MSYS2](https://www.msys2.org/) for GCC and other Unix tools on Windows.

## Setup Instructions

1. **Install MSYS2 and GCC:**

   - Download and install MSYS2 from the official website.
   - Update packages and install `mingw-w64` toolchain.

     ```bash
     pacman -Syu
     pacman -S mingw-w64-ucrt-x86_64-gcc
     ```

2. **Install VSCode and Extensions:**

   - Install Visual Studio Code.
   - Install the C/C++ extension by Microsoft.

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/password-manager.git
   ```

4. **Set Up Dependencies:**

   - **GLFW:** Download and build.
   - **GLAD:** Generate loader and place files in `gui/GLAD/`.
   - **Dear ImGui:** Clone repository and add files to `gui/ImGui/`.

5. **Configure VSCode:**

    1. **Copy Configuration Files**:
        - Navigate to the `.vscode` directory.
        - Copy `tasks.json.example` and `launch.json.example`.
        - Rename them to `tasks.json` and `launch.json` respectively.

    2. **Update Paths**:
        - Edit `tasks.json` and `launch.json` to replace any placeholder paths (e.g., `path-to-msys2`).

    3. **Ignore Personal Configurations**:
        - To avoid committing personal configurations, (which may include machine-specific paths or sensitive data) ensure the following entries are in your `.gitignore`:

        ```plaintext
        .vscode/tasks.json
        .vscode/launch.json
        ```    

    4. **Build and Run**:
        - Press `Ctrl+Shift+B` to build the project.
        - Press `F5` to run the application.

6. **Build and Run:**

   - Open the project folder in VSCode.
   - **Build:** Press `Ctrl+Shift+B` and select "Build Entire Project".
   - **Run:** Press `F5` to start debugging.

---

