/*
VER:
    1. Basic password generation
    2. Create data structure to hold existing password in file to ensure none match
    2. Specify length of password to be generated
    3. Provide user control for characters to not include

*/

#include <iostream>
#include <string>
#include <random>       //bring in random library for better random generation than rand()
#include "../include/PasswordGenerator.h"

//constructor to generate password when object is instantiated
PasswordGenerator::PasswordGenerator() {
    password = generatePassword();
}

//getter
std::string PasswordGenerator::getPassword() const {
    return password;
}

//generate random index int
int PasswordGenerator::randomIndexGenerator() {
    static std::random_device rd;       //seed; non-deterministic: pulled from hardware; unsigned int
    static std::mt19937 gen(rd());     //generator; random_device + mt19937 = random sequence everytimel; mt19937: mersenne twist, high quality PRNG, Conventional Use, 32-bit range
    std::uniform_int_distribution<> dist(0, 89);  //distributor: maps 32-bit sequence from mt19937 to specified range; 90 slots given string charSet
    int randomIndex;
    return randomIndex = dist(gen);        //executes generator and distributor to get random value
}

//generate password string
std::string PasswordGenerator::generatePassword() {
    std::string charSet= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}()[]:;#^,.?!|&_`'~@$%/+*-=";
    std::string createdPassword;

    for (int i = 0; i < 16; i++) {
        int index = randomIndexGenerator();         // call method to get random index
        char randomCharacter = charSet[index];      //acquire character at random index from set character list
        createdPassword += randomCharacter;        //append to createdPassword
    }

    return createdPassword;
};
