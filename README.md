# CryptKey - ! WARNING: these are all temporary placeholders, will finalize later ! 

## PROJECT REQS:
    • Ensure test cases for each component 
    • create use case & activity & crc diagram
    • Comment code; descriptive identifiers/names, comment at TOP of file w/ student name, email, assignment name
    • Assignments MUST have README.TXT, summarizing and documenting work submitted
    
## Proper Usage:
1. Store executable on usb with csv file in root directory of USB
2. Run from USB 
3. Open CSV file and manually find entry as its alphabetical
    a. NOTE: using Excel makes copy and pasting username and password efficient
KEY: Keep it lightweight and portable!

## Security Layers: 
- Must consider tradeoff between convenience & portability vs security
1. Physical attachment to self via carabiner
2. Airtag tracking
3. USB w/ built in PIN function 
4. Encryption to decrypt CSV through password 

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

3. **Keep feature branch up to date: SYNC with latest of remote feature & main branch**
```
git pull --rebase       # 1. keep local feature updated to remote feature 
# OR
git fetch origin        # 2. keep local feature up to date with remote main
git rebase origin/main
```

4. **Push feature branch**
```
git push origin feature-branch
```

5. **Merge feature branch into main: use Pull Requests**
  - Rebase on feature branch before opening pull request to update to latest at main  
```
  git fetch origin
  git rebase origin/main

```
  - Go to GitHub, open Pull Request (PR) from feature-branch -> main; address any merge conflicts
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

### Build the Project - TBA - CONSIDER CREATING BINARY TO LOAD ONTO USB

### Running the Application

## Usage

### GUI Interface:

## Project Structure

- `src/`: Contains the source code (.cpp files).
- `include/`: Contains the header files (.h files).
- `gui/`: Contains GUI-related source files and third-party libraries.
- `.vscode/`: Contains VSCode configuration files.
- `build/`: Contains the compiled executable and build artifacts.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments


--


