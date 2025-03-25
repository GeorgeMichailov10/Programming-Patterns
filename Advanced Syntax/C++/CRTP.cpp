// Curiously Recurring Template Pattern allows static polymorphism (compile time polymorphism) rather than run time, so much faster because
// no need for virtual table lookups.

#include <type_traits>
#include <iostream>

template <typename Derived>
class Base {
public:
    void interface() {
        static_cast<Derived*>(this)->implementation();
    }
};

// Derived class inherits and passes itself as an argument which lets base class know about derived class and compile time and call it directly.
class Derived1 : public Base<Derived1> {
public:
    void implementation() {
        std::cout << "Derived 1" << std::endl;
    }
};

int main() {
    Derived1 d;
    d.interface();    // Calls Derived1 implementation and avoids any virtual function overhead.
    return 0;
}