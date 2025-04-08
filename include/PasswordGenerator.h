#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public:
    // Constructor that accepts customization options.
    // Defaults: length 16, include uppercase, numbers and special characters are true.
    PasswordGenerator(int length = 16, bool includeUppercase = true, bool includeNumbers = true, bool includeSpecialChars = true, const std::string &excludedChars = "");

    // Overloaded constructor to directly supply a custom password.
    PasswordGenerator(const std::string &customPassword);

    std::string getPassword() const;

private:
    std::string m_password;
    int randomIndexGenerator(int max);
    std::string generatePassword(int length, bool includeUppercase, bool includeNumbers, bool includeSpecialChars, const std::string &excludedChars);
};

#endif