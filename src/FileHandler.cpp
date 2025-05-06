#include <fstream>
#include <filesystem>
#include <stdexcept>
#include <vector>
#include <algorithm>
#include "../include/FileHandler.h"


FileHandler::FileHandler() {
    if (!fileExists()) {
        createFile();
    }
}

bool FileHandler::fileExists() {
    return std::filesystem::exists(password_file);
}

bool FileHandler::fileOpens() {
    std::ofstream file(password_file, std::ios::app);
    return file.is_open();
}

void FileHandler::checkFile() {
    if (!fileExists()) {
        createFile();
    }
}

void FileHandler::createFile() {
    std::ofstream file(password_file);
    if (!file.is_open()) {
        throw std::runtime_error("Unable to create file");
    }
}

std::vector<std::string> FileHandler::loadData() {
    checkFile();
    std::vector<std::string> entries;
    std::ifstream inFile(password_file);
    std::string line;
    while (std::getline(inFile, line)) {
        if (!line.empty())
            entries.push_back(line);
    }
    inFile.close();
    return entries;
}

std::string FileHandler::createEntry(const std::string &site, const std::string &username) {
    PasswordGenerator pg;
    std::string password = pg.getPassword();
    return "\"" + site + "\",\"" + username + "\",\"" + password + "\"";
}

bool FileHandler::entryExists(const std::string &site) {
    std::vector<std::string> entries = loadData();
    for (const auto &entry : entries) {
        size_t pos = entry.find(',');
        if (pos != std::string::npos) {
            std::string existingSite = entry.substr(0, pos);
            if (existingSite == site)
                return true;
        }
    }
    return false;
}

bool FileHandler::saveData(const std::string &newEntry, bool overwrite) {
    checkFile();
    std::vector<std::string> entries = loadData();     // Load current entries from the file
    size_t pos = newEntry.find(',');    // Extract website from newEntry
    std::string newSite = (pos != std::string::npos) ? newEntry.substr(0, pos) : "";
    bool found = false;    // Check for an existing entry and update or cancel based on the overwrite flag
    for (auto &entry : entries) {
        size_t posEntry = entry.find(',');
        std::string site = (posEntry != std::string::npos) ? entry.substr(0, posEntry) : "";
        if (site == newSite) {
            if (!overwrite)
                return false;  // Duplicate found BUT no overwrite chosen
            entry = newEntry;  // Overwrite existing entry
            found = true;
            break;
        }
    }
    if (!found) {
        entries.push_back(newEntry);
    }
    
    // Sort entries alphabetically by website for every new entry added
    std::sort(entries.begin(), entries.end(), [](const std::string &a, const std::string &b) {
        size_t posA = a.find(',');
        size_t posB = b.find(',');
        std::string siteA = (posA != std::string::npos) ? a.substr(0, posA) : a;
        std::string siteB = (posB != std::string::npos) ? b.substr(0, posB) : b;
        return siteA < siteB;
    });
    
    // write all sorted entries back to the file (overwriting the file).
    std::ofstream outFile(password_file, std::ios::trunc);
    if (!outFile.is_open()) {
        throw std::runtime_error("Failed to open file for writing");
    }
    for (const auto &entry : entries) {
        outFile << entry << "\n";
    }
    outFile.close();
    return true;
}