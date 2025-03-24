#include <iostream>

// Normally, there is protections on consts and they can't be changed.
// However, this can be bypassed by creating an int pointer directly to the memory address and changing it from the source.
int main() {
    const int num = 10;

    int *ptr = (int *)&num; 
    *ptr = 20;
    std::cout << num;
    return 0;
}