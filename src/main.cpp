// main.cpp
#include <iostream>
#include <string>
#include "FileHandler.h"

int main(int argc, char* argv[]) {
    std::string site, username;
    bool overwrite = false;
    bool dryRun = false;

    // parse CLI arguments.
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];
        if (arg == "--site" && i + 1 < argc) {
            site = argv[++i];
        } else if (arg == "--username" && i + 1 < argc) {
            username = argv[++i];
        } else if (arg == "--overwrite") {
            overwrite = true;
        } else if (arg == "--dry-run") {
            dryRun = true;
        }
    }

    // validate required inputs.
    if (site.empty() || username.empty()) {
        std::cerr << "Usage: " << argv[0]
                  << " --site <website> --username <username> [--overwrite] [--dry-run]" << std::endl;
        return 1;
    }

    FileHandler fh;
    std::string newEntry = fh.createEntry(site, username);

    // always check for duplicates first.
    if (fh.entryExists(site) && !overwrite) {
        std::cerr << "Entry for this site already exists" << std::endl;
        return 1;
    }

    if (dryRun) {
        // In dry run mode, output the generated entry without saving; just for the check
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
