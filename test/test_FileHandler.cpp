#include <cassert>
#include <iostream>
#include <fstream>
#include <cstdio> 
#include "FileHandler.h"


int main() {
    // Prep: Clean any preexisting test file and create FileHandler instance to create file
    std::remove("user_data.csv");
    FileHandler fh;
    {
        std::ifstream file("user_data.csv");
        assert(file.good());
    }

    // Test 1: load data and ensure file empty initially
    auto entries = fh.loadData();
    assert(entries.size() == 0);

    // Test 2: create entry, return string in expected format
    std::string site = "example.com";
    std::string username = "username";
    std::string entry = fh.createEntry(site, username);
    size_t pos1 = entry.find(",");
    size_t pos2 = entry.find(",", pos1 + 1);
    assert(pos1 != std::string::npos);
    assert(pos2 != std::string::npos);

    // Test 3: check if entry exists, should be false initially
    assert(fh.entryExists(site) == false);

    // Test 4: Save entry (no duplicate exists), should return true
    bool saveResult = fh.saveData(entry, false);
    assert(saveResult == true);
    assert(fh.entryExists(site) == true);     // entryExists should now return true

    // Test 5: duplicate save without overwrite, should return false
    std::string newEntry = fh.createEntry(site, username);
    bool saveResult2 = fh.saveData(newEntry, false);
    assert(saveResult2 == false);

    // Test 6: duplicate save with overwrite, should update and return true
    bool saveResult3 = fh.saveData(newEntry, true);
    assert(saveResult3 == true);

    // Test 7: ensure alphabetical sorting, add another entry with site that sorts before "example.com"
    std::string entry2 = fh.createEntry("aaa.com", "anotheruser");
    bool saveResult4 = fh.saveData(entry2, false);
    assert(saveResult4 == true);
    auto entriesSorted = fh.loadData();
    assert(entriesSorted.size() >= 2);     // The 1st entry should start with "aaa.com"
    assert(entriesSorted[0].substr(0, 7) == "aaa.com");

    // clean up test file and ensure test completion
    // std::remove("user_data.csv"); 
    std::cout << "All FileHandler tests passed.\n";
    return 0;
}
