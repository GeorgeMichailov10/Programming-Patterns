def first():
    print("Original behavior")

def second():
    print("New behavior")

first()
first.__code__ = second.__code__
first()
# first was changed to have the behavior of the second function.