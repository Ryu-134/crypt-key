
#include <iostream>
#include <cassert> 
#include <unordered_set>
#include <string> 
#include "PasswordGenerator.h"

int main() {
    // Test 1: Verify password length
    PasswordGenerator pg;
    std::string password = pg.getPassword();
    assert(password.size() == 16 && "Password should be 16 characters long");
    std::cout << "Generated password: " << password << std::endl;

    // Test 2: Consistency Test 
    std::string passwordAgain = pg.getPassword();
    assert(password == passwordAgain && "Password should be constsistent for same instance");
    std::cout << "Password 1: " << password << " Password 2: " << passwordAgain << std::endl; 
    std::cout << "Password is consistent given same instance/seed.\n";

    // Test 3: Uniqueness Test 
    const int uniqueTest = 1000;
    std::unordered_set<std::string> uniquePasswords;      // use set data structure to have it validate uniqueness
    for (int i = 0; i < uniqueTest; i++) {
        PasswordGenerator pgInstance;
        uniquePasswords.insert(pgInstance.getPassword());
    }
    // Expect most passwords to be unique; currently set at 99.5% uniqueness req
    assert(uniquePasswords.size() >= 995 && "Expected at least 995 unique passwords out of 1000 instances");
    std::cout << "Passwords generated in 1000 instances were unique at least 99.5% of the time\n";

    // Test 4: Custom Length Test
    int customLength = 24;
    PasswordGenerator customGen(customLength);
    std::string customPassword = customGen.getPassword();
    assert(customPassword.size() == customLength && "Password must be length as specified");
    std::cout << "Custom length password of length " << customLength << " characters: " << customPassword << std::endl;

    std::cout << "All tests passed!" << std::endl;
    return 0;

}