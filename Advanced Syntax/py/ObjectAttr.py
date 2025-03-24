class Obj:
    def __init__(self):
        self.a = 10
        self.b = "ELP"

obj = Obj()
print(obj.__dict__)
# Prints the object's attributes as a dictionary.