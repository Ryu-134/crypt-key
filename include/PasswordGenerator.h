#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public: 
    // upon instantiation generate password; defaults to 16 char but length and special char inclusion can be customized
    PasswordGenerator(int length = 16, bool removeSpecialChar = false); 
    std::string getPassword() const;

private:
    std::string password;
    int randomIndexGenerator(int max);      // parameter to determine max value based on charSet length
    std::string generatePassword();     
    std::string generatePassword(int length);     
    std::string generatePassword(int length = 16, bool removeSpecialChar = false);     
};

#endif