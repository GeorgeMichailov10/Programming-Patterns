class Old:
    def __call__(self, *args, **kwds):
        print("Old")

class New:
    def __call__(self, *args, **kwds):
        print("New")

obj = Old()
obj()
obj.__class__=New
obj()