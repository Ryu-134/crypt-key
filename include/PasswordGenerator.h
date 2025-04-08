#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public:
    // New constructor that accepts customization options.
    // By default, include uppercase letters, numbers, and special characters.
    PasswordGenerator(int length = 16, bool includeUppercase = true, bool includeNumbers = true, bool includeSpecialChars = true, const std::string &excludedChars = "");

    // Overloaded constructor for a custom (user-supplied) password.
    PasswordGenerator(const std::string &customPassword);

    std::string getPassword() const;

private:
    std::string m_password;
    int randomIndexGenerator(int max);
    std::string generatePassword(int length, bool includeUppercase, bool includeNumbers, bool includeSpecialChars, const std::string &excludedChars);
};

#endif