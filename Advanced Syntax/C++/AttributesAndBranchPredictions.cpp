#include <iostream>

// Attributes like [[nodiscard]] will throw warnings if the return value from a function labelled with this is ignored.
// Branch Prediction hints tell the compiler which branch is more likely so can help optimize cpu performance.

[[nodiscard]] int getSquareIfNotDivisibleBySeven(int n) {
    if (n % 7) [[likely]] {
        return n * n;
    } else [[unlikely]] {
        return 0;
    }
}

int main() {
    // Example to show warning during compilation
    getSquareIfNotDivisibleBySeven(5);

    // Example for likely not likley
    std::cout << getSquareIfNotDivisibleBySeven(7) << getSquareIfNotDivisibleBySeven(5) << std::endl;
}