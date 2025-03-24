#include <stdio.h>
#include <stdlib.h>
#include <iostream>

void after() {
    std::cout << "Printing upon termination." << std::endl;
}

int main() {
    std::atexit(after); // This gets called at the end right before the program terminates.
    std::cout << "Main" << std::endl;
    return 0;
}