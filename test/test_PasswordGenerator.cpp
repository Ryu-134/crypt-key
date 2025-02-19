
#include <iostream>
#include <cassert> 
#include <unordered_set>
#include <string> 
#include "PasswordGenerator.h"

int main() {
    // Test 1: Verify password length
    PasswordGenerator pg;
    std::string password = pg.getPassword();
    std::cout << "Generated password: " << password << std::endl;
    assert(password.size() == 16 && "Password should be 16 characters long");

    // Test 2: Consistency Test 
    std::string passwordAgain = pg.getPassword();
    assert(password == passwordAgain && "Password should be constsistent for same instance");
    std::cout << "Password is consistent given same instance/seed.\n";
    std::cout << "Password 1: " << password << " Password 2: " << passwordAgain << "\n"; 

    // Test 3: Uniqueness Test 
    const int uniqueTest = 1000;
    std::unordered_set<std::string> uniquePasswords;      // use set data structure to have it manage uniqueness
    for (int i = 0; i < uniqueTest; i++) {
        PasswordGenerator pgInstance;
        uniquePasswords.insert(pgInstance.getPassword());
    }
    // Expect most passwords to be unique; currently set at 99% uniqueness req
    assert(uniquePasswords.size() >= 990 && "Expected at least 990 unique passwords out of 1000 instances");
    std::cout << "Passwords generated in 1000 instances were unique at least 99% of the time\n";

    std::cout << "All tests passed!" << std::endl;
    return 0;

}