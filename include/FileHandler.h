#ifndef FILEHANDLER_H
#define FILEHANDLER_H


#include <string>
#include <vector>
#include "PasswordGenerator.h"


class FileHandler {
private:
    const std::string password_file = "user_data.csv";
    void checkFile();
    bool fileExists();
    bool fileOpens();
    void createFile();

public:
    FileHandler();
    std::vector<std::string> loadData();  
    std::string createEntry(const std::string &site, const std::string &username); // Create entry in format: "website, username, password"
    bool entryExists(const std::string &site);
    bool saveData(const std::string &newEntry, bool overwrite);
};


#endif
