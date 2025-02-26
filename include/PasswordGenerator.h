#ifndef PASSWORDGENERATOR_H
#define PASSWORDGENERATOR_H

#include <string>

class PasswordGenerator {
public: 
    /* Options:
       PasswordGenerator pg;                        // defaults to 16 and special chars included
       PasswordGenerator pg(20);                    // 20-char password, special chars included
       PasswordGenerator pg(20, true);              // 20-char password, no special characters (only digits/letters)
       PasswordGenerator pg(20, false, "@#$");      // 20-char password, special chars included but exclude '@', '#', '$'
    */ 
    PasswordGenerator(int length = 16, bool excludeSpecialChars = false, const std::string& excludedChars = ""); 
main
    std::string getPassword() const;

private:
    std::string m_password;
    int randomIndexGenerator(int max);      // parameter to determine max value for distribution based on charSet length
    std::string generatePassword(int length, bool excludeSpecialChars, const std::string& excludedChars);     
};

#endif
