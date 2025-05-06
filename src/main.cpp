#include <iostream>
#include <string>
#include "../include/FileHandler.h"
#include "../include/PasswordGenerator.h"

int main(int argc, char* argv[]) {
    std::string site, username;
    int length = 16;                   // Default password length
    bool includeUppercase = true;      // Default: include uppercase letters
    bool includeNumbers = true;        // Default: include digits
    bool includeSpecialChars = true;   // Default: include special characters
    bool overwrite = false;
    bool dryRun = false;
    std::string how = "Random";       // Default: Random
    std::string customPassword = "";

    // Parse command-line arguments:
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "--site" && i + 1 < argc) {
            site = argv[++i];
        } else if (arg == "--username" && i + 1 < argc) {
            username = argv[++i];
        } else if (arg == "--length" && i + 1 < argc) {
            length = std::stoi(argv[++i]);
        } else if (arg == "--no-uppercase") {
            includeUppercase = false;
        } else if (arg == "--no-numbers") {
            includeNumbers = false;
        } else if (arg == "--excludeSpecial") {
            includeSpecialChars = false;
        } else if (arg == "--overwrite") {
            overwrite = true;
        } else if (arg == "--dry-run") {
            dryRun = true;
        } else if (arg == "--how" && i + 1 < argc) {
            how = argv[++i];
        } else if (arg == "--custom-password" && i + 1 < argc) {
            customPassword = argv[++i];
        }
    }

    if (site.empty() || username.empty()) {
        std::cerr << "Usage: " << argv[0]
                  << " --site <website> --username <username> [--length <num>] [--no-uppercase] [--no-numbers] [--excludeSpecial] [--overwrite] [--dry-run] [--how <Custom|Random>] [--custom-password <password>]"
                  << std::endl;
        return 1;
    }

    std::string password;
    if (how == "Custom" && !customPassword.empty()) {
        password = customPassword;
    } else {
        PasswordGenerator pg(length, includeUppercase, includeNumbers, includeSpecialChars, "");
        password = pg.getPassword();
    }

    // Create a CSV entry (make sure there is no extra comma).
    // Quoting each field protects against internal commas.
    std::string csvLine = "\"" + site + "\",\"" + username + "\",\"" + password + "\"";

    // If dry-run, output the generated entry without saving.
    if (dryRun) {
        std::cout << csvLine << std::endl;
        return 0;
    }

    // Otherwise, use FileHandler to save the entry.
    FileHandler fh;
    if (fh.entryExists(site) && !overwrite) {
        std::cerr << "Entry for this site already exists" << std::endl;
        return 1;
    }

    bool success = fh.saveData(csvLine, overwrite);
    if (success) {
        std::cout << csvLine << std::endl;
        return 0;
    } else {
        std::cerr << "Failed to save the new entry." << std::endl;
        return 1;
    }
}