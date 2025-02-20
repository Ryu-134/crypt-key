/*
FAQ: this is backend logic for password manager using gui; MUST develop with gui use in mind (parameters and returns)
--------
TODO:

    3. Provide user control for characters to not include (some special characters may not be allowed on webpages)
    4. Provide sub option for user to type in own custom password
    5. Add option to remove special characters entirely simply with one click 

    FOR LATER: Create data structure to hold existing password in file to ensure none match and prompt user if enrty already exists to give option to overwrite or cancel

*/

#include <iostream>
#include <string>
#include <random>       // bring in random library for better random generation than rand()
#include "PasswordGenerator.h"

// default constructor to generate password of 16-char length
PasswordGenerator::PasswordGenerator() {
    password = generatePassword(16);
}

// constructor when password length  specified
PasswordGenerator::PasswordGenerator(int length) {
    password = generatePassword(length);
}

// getter
std::string PasswordGenerator::getPassword() const {
    return password;
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
std::string PasswordGenerator::generatePassword(int length) {
    std::string charSet= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}()[]:;#^,.?!|&_`'~@$%/+*-=";
    std::string createdPassword;
    int charSetLength = charSet.size();     // get length of charSet to be used for password

    for (int i = 0; i < length; i++) {
        int index = randomIndexGenerator(charSetLength);         // call method to get random index
        char randomCharacter = charSet[index];      // acquire character at random index from set character list
        createdPassword += randomCharacter;        // append to createdPassword
    }

    return createdPassword;
};
