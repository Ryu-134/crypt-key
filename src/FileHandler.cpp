/*
Ver:
1. General functionality to check existence, load, save, prompt
2. Create userInput function for y/n prompts
3. Move cout/cin into main
4. update so entryExists can overwrite existing entry isntead of exiting program
2. Add option for where to check for file existence
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
