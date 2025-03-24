#include <iostream>
#include <algorithm>
#include <utility>
#include <type_traits>

class Buffer {
public:
    int *data;
    size_t size;

    Buffer(size_t s) : size(s) {
        data = new int[s];
    }

    // Copy Constructor: Creates deep copy of object
    Buffer(const Buffer& other) : size(other.size) {
        data = new int[other.size];
        std::copy(other.data, other.data + other.size, data);
    }

    // Move Constructor: Essentially steals the identity/state of the other and leaves it empty.
    Buffer(Buffer&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }

    ~Buffer() {
        delete[] data;
    }
};

// lvalue: locator value, has a name and an address and persists beyond just the current expression, typically on left hand side.
// rvalue: Read value, temporary and doesn't persist, can only appear on right-hand side.
// ie x = 5; x is lvalue, 5 is rvalue.
// This template will call the appropriate constructor on our behalf.
template <typename... Args>
Buffer makeBuffer(Args&&... args) {
    return Buffer(std::forward<Args>(args)...)
}