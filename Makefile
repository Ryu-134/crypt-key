CXX = g++
CXXFLAGS = -std=c++17 -Wall -I include
TARGET = password_manager
SOURCES = src/main.cpp src/FileHandler.cpp src/PasswordGenerator.cpp
HEADERS = include/FileHandler.h include/PasswordGenerator.h

all: $(TARGET)

$(TARGET): $(SOURCES) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -f $(TARGET)
