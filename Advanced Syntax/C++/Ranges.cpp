#include <iostream>
#include <vector>
#include <ranges>

// range::views is a super useful option added into C++20 for working with iterable objects
/*
-> filter keeps only elements that match condition like below
-> transform applies a function to each element (ie multiplying or squaring etc)
-> take(n) takes the first n elements
-> drop(n) skips the first n elements
-> reverse
-> iota(start, stop) like Pythons range function
*/
// Can also stack multiple on each other like below:


int main() {
    std::vector<int> numbers = {1,2,3,4,5,6};
    auto even_sq = numbers 
        | std::ranges::views::filter([](int n) { return n % 2 == 0; })
        | std::ranges::views::transform([](int n) { return n*n; });
        
    for (int num : even_sq) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}