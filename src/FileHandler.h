#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <string>
#include "PasswordGenerator.h"

class FileHandler
{
private:
  const std::string password_file = "user_data.csv";
  void checkFile();
  bool fileExists();
  bool fileOpens();
  void createFile();

public:
  FileHandler();
  void execute();
  void loadData();
  std::string formatEntry();
  void saveData(const std::string &newEntry);
  void entryExists(const std::string &siteForPassword);
  std::string getCurrentDateAndTime();
};

#endif
