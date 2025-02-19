/* FAQ: develop with gui in mind; use parameters and return to separate frontend and backend
*/

/*
Ver:
1. General functionality to check existence, load, save
2. Move cout/cin into main; separate front and back end
3. update so entryExists (or other) can overwrite existing entry instead of exiting program
  a. prompt user to overwrite or cancel
4. Add option for where to check for file existence OR omit if we can make .exe within usb
3. Add option where to output file too (USB drive)
*/

#include <iostream>
#include <fstream>
#include <filesystem>
#include <stdexcept>

#include "FileHandler.h"

void FileHandler::checkFile()
{
  if (!std::filesystem::exists(password_file))
  {
    std::cout << "File does not exist. Creating new file...\n";
    std::ofstream file(password_file);
  }
}

// create file
void FileHandler::createFile()
{
  if (!guiMode && std::cin.good())
  {
    while (true)
    {
      std::cout << "Would you like to create a file?\n"
                << "Enter y or n.\n";
      std::string userConfirmation;
      std::getline(std::cin, userConfirmation);

      if (userConfirmation.length() != 1)
      {
        std::cout << "Invalid input.\nPlease enter y or n.\n";
        continue;
      }

      char userChar = std::tolower(userConfirmation[0]);
      if (userChar == 'y')
      {
        std::ofstream file(password_file);
        break;
      }
      else if (userChar == 'n')
      {
        std::cout << "File creation aborted.\n";
        throw std::runtime_error("User aborted file creation");
      }
      else
      {
        std::cout << "Invalid input.\nPlease enter y or n.\n";
        continue;
      }
    }
  }
  else
  {
    std::ofstream file(password_file);
  }
};

// check if file exists to load
void FileHandler::loadData()
{
  checkFile();
};

// creating and formatting entry to add
std::string FileHandler::formatEntry()
{
  std::string userInputSite;
  std::string userInputUsername;

  std::cout << "Enter site: \n";
  std::getline(std::cin, userInputSite);
  std::cout << "Checking if entry does not already exist\n";
  entryExists(userInputSite);

  std::cout << "Enter username: \n";
  std::getline(std::cin, userInputUsername);

  std::string currentDate = getCurrentDateAndTime();
  PasswordGenerator newPassword;
  std::string password = newPassword.getPassword();

  std::cout << "Here is your entry: (site , username, password, date)\n";
  std::string newEntry = userInputSite + ", " + userInputUsername + ", " + password + ", " + currentDate;
  std::cout << newEntry << "\n";
  return newEntry;
};

// save new password entry and send confirmation
void FileHandler::saveData(const std::string &newEntry)
{
  if (!guiMode && std::cin.good())
  { // check if cin is connected (console application)
    while (true)
    {                               // for console
      std::string userConfirmation; // string type instead of char, to only use getline
      std::cout << "Would you like to save entry?\n"
                << "Enter y or n.\n";
      std::getline(std::cin, userConfirmation);

      if (userConfirmation.length() != 1)
      { // check input validity
        std::cout << "Invalid input,\nPlease enter y or n.\n";
        continue; // begin next loop
      }

      char userChar = std::tolower(userConfirmation[0]); // normalize case
      if (userChar == 'n')
      {
        std::cout << "Entry not saved.\n";
        return;
      }
      else if (userChar == 'y')
      {
        checkFile();
        std::ofstream file(password_file, std::ios::app); // append entry
        file << newEntry << "\n";
        std::cout << "New password entry successfully added.\n";
        return;
      }
      else
      {
        std::cout << "Invalid input,\nPlease enter y or n.\n";
        continue;
      }
    }
  }
  else
  {
    checkFile();
    std::ofstream file(password_file, std::ios::app);
    if (!file.is_open())
    {
      throw std::runtime_error("Failed to open file for writing");
    }
    file << newEntry << "\n";
    file.close();
  }
};

// read CSV file to see if password doesnt already exist
void FileHandler::entryExists(const std::string &siteForPassword)
{
  std::string line;
  std::ifstream file(password_file);

  if (!file.is_open())
  {
    throw std::runtime_error("Failed to open file for reading");
  }

  while (std::getline(file, line))
  {
    size_t pos = line.find(',');
    if (pos != std::string::npos)
    {                                         // is ',' was found proceed; std::string:npos = no position (i.e. not found)
      std::string site = line.substr(0, pos); // extract substring from '0 - ,' as site is first entry in each line
      if (siteForPassword == site)
      {
        std::cout << "Entry already exists.\n";
        return;
      }
    }
  }

  std::cout << "Entry does not exist in file.\n";
};

// get date to add to entry
std::string FileHandler::getCurrentDateAndTime()
{
  time_t now = time(0); // time_t, data type to represent time as int; gives time in seconds from 1/1/1970
  char buf[80];
  strftime(buf, sizeof(buf), "%m-%d-%Y", localtime(&now)); // localtime(&now) converts 'now' into struct tm*
  return std::string(buf);                                 // convert char arrray into string; NOT type casting
};
