#include "../include/PasswordGenerator.h"
#include <algorithm>
#include <random>

// Constructor that uses custom parameters to generate a password
PasswordGenerator::PasswordGenerator(int length, bool includeUppercase, bool includeNumbers, bool includeSpecialChars, const std::string &excludedChars) {
    m_password = generatePassword(length, includeUppercase, includeNumbers, includeSpecialChars, excludedChars);
}

// Overloaded constructor that simply uses a custom provided password
PasswordGenerator::PasswordGenerator(const std::string &customPassword) : m_password(customPassword) {
}

std::string PasswordGenerator::getPassword() const {
    return m_password;
}

int PasswordGenerator::randomIndexGenerator(int max) {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, max - 1);
    return dist(gen);
}

std::string PasswordGenerator::generatePassword(int length, bool includeUppercase, bool includeNumbers, bool includeSpecialChars, const std::string &excludedChars) {
    // Start with lowercase letters as baseline.
    std::string charSet = "abcdefghijklmnopqrstuvwxyz";
    
    if (includeUppercase) {
        charSet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }
    if (includeNumbers) {
        charSet += "0123456789";
    }
    if (includeSpecialChars) {
        charSet += "{}()[]:;#^,.?!|&_`'~@$%/+*-=";
    }
    
    // Remove any excluded characters.
    for (char c : excludedChars) {
        charSet.erase(std::remove(charSet.begin(), charSet.end(), c), charSet.end());
    }
    
    if (charSet.empty()) {
        return "";
    }
    
    std::string createdPassword;
    int charSetLength = charSet.size();
    for (int i = 0; i < length; i++) {
        int index = randomIndexGenerator(charSetLength);
        createdPassword += charSet[index];
    }
    return createdPassword;
}