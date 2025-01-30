# Offline Password Manager Project Documentation

## 1. Introduction


Develop a C++ password manager that operates entirely offline. The application will:

- Generate complex passwords locally.
- Store passwords in an Excel-compatible file (like CSV) on a user-specified location (e.g., a USB drive).
- Preserve and update existing data without any data loss.
- Provide a basic graphical user interface (GUI) for easy interaction.

---

## 2. Project Objectives

### Core Features:

- **Offline Functionality**
- **Complex Password Generation**
- **Secure Storage**
- **User-Controlled File Location:** For reading and writing.
- **Data Preservation:** Update existing files without overwriting or erasing existing data.
- **Entry Modification:** Enable modification of existing entries if the site already exists.

### User Interface:

- Implement a simple GUI for intuitive user interaction.

---

## 3. Project Structure

```
PasswordManager/
├── src/               # Source code files (.cpp)
├── include/           # Header files (.h)
├── gui/               # GUI (icons, images)
├── data/              # Data files (e.g., CSV)
├── doc/               # Documentation
├── build/             # Compiled binaries
├── README.md          # Project overview
```

---

## 4. Key Components

### Classes

- **PasswordGenerator:**
  - Generates complex passwords locally.
- **FileHandler:**
  - Manages reading and writing to the local CSV file.
  - Ensures existing data isn't overwritten.
- **GUI:**
  - Provides the graphical interface for offline user interaction.

---

## 5. Implementation Steps

**Step 1: Set Up Project**

- Create the directory structure.
- Initialize a Git repository (optional if staying entirely offline).
- Write a basic `README.md`.

**Step 2: Implement Core Functionality (Console Version)**

- Develop `PasswordGenerator` to create passwords.
- Develop `FileHandler` to manage CSV files locally.
- Create a simple `main.cpp` to tie everything together.

**Step 3: Testing and Exception Handling**

- Test the entire implementation prior to beginning GUI integration.
- Add error checking and exception handling.

**Step 4: Add Basic GUI**

- Install and set up a GUI framework (ImGui).
- Design 'gui.cpp' as a simple interface with input fields and buttons.
- Connect GUI elements to backend functions.
- Validate user inputs in the GUI.

**Step 5: Testing**

- Manually test the application to ensure it works as expected offline.
- Set up unit tests for core components.

---

## 6. Basic GUI Design

- **Main Window:**
  - Input fields for site name, username, and password length.
  - Buttons for generating passwords, saving entries, exiting program.
  - Messages to display success or error notifications.

---

## 7. Security Considerations

- **Offline Security:**
  - By keeping all operations offline, you reduce the risk of external attacks.
  - Ensure that sensitive data is stored securely on the local device.

---

## 8. Future Enhancements

- **Data Encryption:** Implement local encryption for stored passwords to enhance security.
  - Use encryption algorithms that do not require internet connectivity.
- **Password Strength Indicator:** Provide feedback on the strength of generated passwords.
- **Search and Filter:** Allow users to search for entries by site or username.
- **User Interface Improvements:** Enhance the GUI with better visuals and usability features.
- **Import/Export Functionality:** Enable importing from and exporting to different local file formats.

---
