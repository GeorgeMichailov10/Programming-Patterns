// Lambda functions are quick unnamed functions that you can define inside of an expression and are super handy.

#include <vector>
#include <iostream>
#include <algorithm>


int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // Example 1: Summing up all of the values in a vector
    int sum = 0;
    std::for_each(vec.begin(), vec.end(), [&sum](int value) -> int { sum += value; });

    // You can also sort, filter, etc. in arrays.
}