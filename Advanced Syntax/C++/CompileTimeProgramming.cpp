/*
Normally, logic happens at runtime (calculations, function calls, etc.) and only types are checked at compile time.
With compile time programming, you offload certain calculations/function calls to the compiler, so it's done at compile time, not execution.
Good for performance, enforcing templates.
*/

#include <iostream>
#include <type_traits>
#include <concepts>

// Only allows add to compile if T is integral type (int, long, size_t, etc.). Enable if restricts the template.
// This is compile time type checking and saves bugs before even running the program.
// SFINAE: Substitution Faillure Is Not An Error
template<typename T>
typename std::enable_if<std::is_integral<T>::value, T>::type add(T a, T b) {
    return a + b;
}

// Very similar to the above, but better.
// Unfortunately, C++20 minimum req, so anything earlier use above.
template<std::integral T>
T multiply(T a, T b) {
    return a * b;
}

// constexpr means that the compiler computes the values of function calls to this specific function at compile time if the inputs are known so saves runtime.
// Best used for computationally heavy logic.
// Great for something like ML where calculation heavy, static things, lookup tables etc, because performance will be so much faster.
// Bad for things like web dev where too dynamic and can't predict/have data on hand at compile time.
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n-1);
}

int main() {
    std::cout << add(3, 4) << std::endl;
    std::cout << multiply(3, 4) << std::endl;
    std::cout << factorial(5) << std::endl;
}

