
#include <iostream>
#include <cassert> 
#include <unordered_set>
#include <string> 
#include <cctype>
#include "PasswordGenerator.h"

int main() {
    // Test 1: Verify password length
    PasswordGenerator pg;
    std::string password = pg.getPassword();
    assert(password.size() == 16 && "Password should be 16 characters long");
    std::cout << "Generated password: " << password << std::endl;

    // Test 2: Consistency  
    std::string passwordAgain = pg.getPassword();
    assert(password == passwordAgain && "Password should be constsistent for same instance");
    std::cout << "Password 1: " << password << " Password 2: " << passwordAgain << std::endl; 
    std::cout << "Password is consistent given same instance/seed" << std::endl;

    // Test 3: Uniqueness  
    const int uniqueTest = 1000;
    std::unordered_set<std::string> uniquePasswords;      // use set data structure to have it validate uniqueness
    for (int i = 0; i < uniqueTest; i++) {
        PasswordGenerator pgInstance;
        uniquePasswords.insert(pgInstance.getPassword());
    }
    // Expect most passwords to be unique; currently set at 99.5% uniqueness req
    assert(uniquePasswords.size() >= 995 && "Expected at least 995 unique passwords out of 1000 instances");
    std::cout << "Passwords generated in 1000 instances were unique at least 99.5% of the time" << std::endl;

    // Test 4: Custom Length 
    int customLength = 32;
    PasswordGenerator customGen(customLength);
    std::string customPassword = customGen.getPassword();
    assert(customPassword.size() == customLength && "Password must be length as specified");
    std::cout << "Custom length password of length " << customLength << " characters: " << customPassword << std::endl;

    // Test 5: Exclude all specials chars
    PasswordGenerator noSpecial(32, true);
    std::string noSpecialCharPass = noSpecial.getPassword();
    for (char c : noSpecialCharPass) {
        assert(std::isalnum(c) && "Password should only contain alphanumeric characters when removeSpecialChar is true");
    }
    std::cout << "Password with no special characters generated: " << noSpecialCharPass << std::endl;

    // Test 6: Exclude Selected Characters 
    std::string excluded = "{}()[]:;#^,.?!|&_`'~@$";     // everything but arithmetic chars excluded
    PasswordGenerator excludeSelected(32, false, excluded);
    std::string excludePass = excludeSelected.getPassword();
    for (char c : excluded) {
        assert(excludePass.find(c) == std::string::npos && "Excluded character found in password");
    }
    std::cout << "Password with selected characters (" << excluded << ") excluded: " << excludePass << std::endl;

    // Test 7: Custom Password 
    std::string customInput = "MyCustomPass123!";
    PasswordGenerator customPasswordGen(customInput);
    std::string customGenerated = customPasswordGen.getPassword();
    assert(customGenerated == customInput && "Custom password should match the user input");
    std::cout << "Custom password correctly set: " << customGenerated << std::endl;

    std::cout << "All tests executed succesfully.\n" << "Exiting unit test program." << std::endl;
    return 0;

}