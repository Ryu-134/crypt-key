#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public: 
    PasswordGenerator();
    std::string getPassword() const;

private:
    std::string password;
    int randomIndexGenerator();
    std::string generatePassword();
};

#endif