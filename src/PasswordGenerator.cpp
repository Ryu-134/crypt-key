/*
FAQ: this is backend logic for password manager using gui; MUST develop with gui use in mind no matter what (parameters and returns)
--------
TODO:
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <random>       // bring in random library for better random generation than rand()
#include "../include/PasswordGenerator.h"

// constructor when password length  specified
PasswordGenerator::PasswordGenerator(int length, bool excludeSpecialChars, const std::string& excludedChars) {
    m_password = generatePassword(length, excludeSpecialChars, excludedChars);
}

// Overloaded constructor for custom password input via GUI
PasswordGenerator::PasswordGenerator(const std::string& customPassword) {
    m_password = customPassword;
}

// getter
std::string PasswordGenerator::getPassword() const {
    return m_password;
}

// generate random index int
int PasswordGenerator::randomIndexGenerator(int max) {
    static std::random_device rd;       // seed; non-deterministic: pulled from hardware; unsigned int
    // generator; random_device + mt19937 = random sequence everytime; mt19937: mersenne twist, high quality PRNG, Conventional Use, 32-bit range
    static std::mt19937 gen(rd());    
    // distributor: maps 32-bit sequence from mt19937 to specified range; (0 ~ max-1) to distribute over password length thats 1-indexed
    std::uniform_int_distribution<> dist(0, max - 1);  
    int randomIndex;
    return randomIndex = dist(gen);        // executes generator and distributor to get random value
}

// generate password string
std::string PasswordGenerator::generatePassword(int length, bool excludeSpecialChars, const std::string& excludedChars) {
    std::string charSet;
    // exclude all special chars if selected
    if (!excludeSpecialChars) {
        charSet= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}()[]:;#^,.?!|&_`'~@$%/+*-=";
    } else {
        charSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }

    // remove chars specified
    for (char c : excludedChars) {
        charSet.erase(std::remove(charSet.begin(), charSet.end(), c), charSet.end());
    }

    std::string createdPassword;
    int charSetLength = charSet.size();     // get length of charSet to be used for password
    for (int i = 0; i < length; i++) {
        int index = randomIndexGenerator(charSetLength);         // call method to get random index
        char randomCharacter = charSet[index];      // acquire character at random index from set character list
        createdPassword += randomCharacter;        // append to createdPassword
    }

    return createdPassword;
};
