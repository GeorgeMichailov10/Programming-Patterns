#include <iostream>
#include <type_traits>

// This is able to dynamically handle adding multiple types, however, these params need both be the same type and able to be added.
template<typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    std::cout << add(3, 4) << std::endl;
    std::cout << add(3.05, 4.05) << std::endl;
}

// See CompileTimeProgramming for more.