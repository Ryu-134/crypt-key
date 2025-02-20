#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public: 
    PasswordGenerator();    // default constructor to give 16 char complex password
    PasswordGenerator(int length);      // constructor when length specified
    std::string getPassword() const;

private:
    std::string password;
    int randomIndexGenerator(int max);      // parameter to determine max value based on charSet length
    std::string generatePassword(int length);     
};

#endif