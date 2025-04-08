#include "../include/PasswordGenerator.h"
#include <algorithm>
#include <random>

// Constructor that generates a password based on customization.
PasswordGenerator::PasswordGenerator(int length, bool includeUppercase, bool includeNumbers, bool includeSpecialChars, const std::string &excludedChars) {
    m_password = generatePassword(length, includeUppercase, includeNumbers, includeSpecialChars, excludedChars);
}

// Constructor that uses the provided custom password.
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
    // Always start with lowercase letters.
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

    // Remove any characters that the user wants to exclude.
    for (char c : excludedChars) {
        charSet.erase(std::remove(charSet.begin(), charSet.end(), c), charSet.end());
    }

    if (charSet.empty()) {
        return "";
    }

    std::string password;
    for (int i = 0; i < length; i++) {
        int idx = randomIndexGenerator(charSet.size());
        password.push_back(charSet[idx]);
    }
    return password;
}