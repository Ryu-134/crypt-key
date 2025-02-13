#ifndef FILEHANDLER_H
#define FILEHANDLER_H

#include <string>

class FileHandler
{
private:
  const std::string password_file = "user_data.csv";
  void checkFile();
};

#endif
