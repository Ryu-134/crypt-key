# CryptKey - ! WARNING: these are all temporary placeholders, will finalize later ! 

## Team Workflow - REMOVE LATER
1. **Create feature branch**:
```
git checkout main         # Switch to main branch
git pull origin main      # Get latest changes
git checkout -b feature-branch # Create a new branch for the feature
```

2. **Work on feature and commit to that branch**
```
git add .
git commit -m "Added new feature X"
```

3. **Keep feature branch up to date: SYNC with latest main branch**
```
git pull --rebase origin main # apply local changes over up to date main 
```

4. **Push feature branch**
```
git push origin feature-branch
```

5. **Merge feature branch into main: use Pull Requests**
  - Rebase on feature branch before opening pull request to update to latest at main
  - Go to GitHub, open Pull Request (PR) from feature-branch -> main
  - Team review, approve, merge PR

6. **After merging feature branch update local main (optionally delete feature branch if applicable)**
```
git checkout main
git pull origin main

```
---

## Project Mission
This is a project for creating an offline password manager in C++ with integrated GUI adhereing to software engineering principles.

**Goal:** Securely, efficiently, and conveniently store passwords locally on the user's machine without internet connectivity.

## Features

- **Offline Use:** Local password storage and exporting
- **Password Generation:** Generates secure passwords using a mix of characters with user customizability.
- **GUI Interfaces:** Offers intuitve graphical user interfaces for ease of use.
- **Data Storage:** Saves password entries to a CSV file (`user_data.csv`).
- **File Handling:** Checks for existing entries and handles file operations.

## Getting Started

### Prerequisites

- **Operating System:** 
- **Compiler:** 
- **Development Environment:** Visual Studio Code (VSCode)
- **Dependencies:**
  - **TBA**

### Installation

1. **Clone the Repository:**

   ```
   git clone https://github.com/Ryu-134/offline-password-manager.git
   ```

2. **Install Dependencies:**

   - **TBA**

3. **Set Up the Directory Structure:**

   Ensure your project directory is organized as follows:

   ```
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
   │   ├── ***TBA***
   ├── .vscode/
       ├── tasks.json
       └── launch.json


4. **Configure VSCode:**

   - Place `tasks.json` and `launch.json` in the `.vscode/` directory.
   - Adjust paths in `tasks.json` and `launch.json` to match your directory structure.

### Build the Project - TBA - CONSIDER CREATING BINARY TO LOAD ONTO USB

### Running the Application

## Usage

### GUI Interface:

1. Launch the application.
2. Enter the site and username in the respective fields.
3. Click "Generate Password" to create a new password.
4. Click "Save Entry" to save the details to `user_data.csv`.
  - a. Append if entry does not exist
  - b. If entry exists prompt user to overwrite or not.


## Project Structure

- `src/`: Contains the source code (.cpp files).
- `include/`: Contains the header files (.h files).
- `gui/`: Contains GUI-related source files and third-party libraries.
- `.vscode/`: Contains VSCode configuration files.
- `build/`: Contains the compiled executable and build artifacts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments


---

# Build Environment Setup

## Prerequisites

- **Operating System:** 
- **Compiler:** 
- **IDE:** Visual Studio Code (VSCode)
- **Dependencies:**
  - **TBA**

- **Tools:**
  - TBA

## Setup Instructions

---

