// Always use smart pointers. They manage memory on your behalf which makes it so much easier not to have leaks and weird memory issues.
// Unique pointers enforce that this object can only have one pointer to this address and does not allow the object to be shared or copied, only moved.
// Shared Pointers allow multiple pointers to the same object with the same full privileges that a unique pointer would have.
// Weak Pointers are only able to view an object and call functions that don't change anything.

#include <iostream>
#include <memory>

struct Object {
    Object() { std::cout << "Object Acquired\n"; }
    ~Object() { std::cout << "Object Destroyed\n"; }

    void signal() const { std::cout << "Signal\n"; }
};

int main() {
    // Unique pointer: Does not allow other owners to this. Can't be shared or copied
    std::unique_ptr<Object> uniqueObj = std::make_unique<Object>();
    uniqueObj->signal();
    std::unique_ptr<Object> movedUniqueObj = std::move(uniqueObj); // Move allowed, copy not allowed

    std::shared_ptr<Object> shared1 = std::make_shared<Object>();
    {
        std::shared_ptr<Object> shared2 = shared1; // Shared ownership of same memory address allowed
        std::cout << "Shared count = " << shared1.use_count() << std::endl;
    }
    std::cout << "Shared count after shared2 iis freed = " << shared1.use_count() << std::endl;

    std::weak_ptr<Object> weakPtr = shared1;
    if (auto locked = weakPtr.lock()) {
        std::cout << "Weak pointer locked. Shared count: " << shared1.use_count() << std::endl;
    } else {
        std::cout << "Object is expired.\n";
    }

    shared1.reset(); // delete it

    if (weakPtr.expired()) {
        std::cout << "Weak ptr has expired\n";
    }

    return 0;
}

