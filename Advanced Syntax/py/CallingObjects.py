class Obj:
    def __call__(self, *args, **kwds):
        print("Object call")

obj = Obj()
obj()