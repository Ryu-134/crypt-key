#include <iostream>
#include <string>
#include "../include/FileHandler.h"
#include "../include/PasswordGenerator.h"

int main(int argc, char* argv[]) {
    std::string site, username;
    int length = 16;
    bool includeUppercase = true;
    bool includeNumbers = true;
    bool includeSpecialChars = true;
    bool overwrite = false;
    bool dryRun = false;

    // Parse command-line arguments.
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
        }
    }

    if (site.empty() || username.empty()) {
        std::cerr << "Usage: " << argv[0]
                  << " --site <website> --username <username> [--length <num>] [--no-uppercase] [--no-numbers] [--excludeSpecial] [--overwrite] [--dry-run]"
                  << std::endl;
        return 1;
    }

    // Create a PasswordGenerator using the custom options.
    PasswordGenerator pg(length, includeUppercase, includeNumbers, includeSpecialChars, "");
    std::string password = pg.getPassword();

    // Use FileHandler to create the entry.
    FileHandler fh;
    // Ensure that when creating the CSV entry, only three fields are produced.
    std::string newEntry = fh.createEntry(site, username);
    
    // Check if entry exists (assuming FileHandler::entryExists does that)
    if (fh.entryExists(site) && !overwrite) {
        std::cerr << "Entry for this site already exists" << std::endl;
        return 1;
    }
    
    if (dryRun) {
        std::cout << newEntry << std::endl;
        return 0;
    }
    
    bool success = fh.saveData(newEntry, overwrite);
    if (success) {
        std::cout << newEntry << std::endl;
        return 0;
    } else {
        std::cerr << "Failed to save the new entry." << std::endl;
        return 1;
    }
}