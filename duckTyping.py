class duck:
    def swim(self):
        print("i am swiming")
    def walk(self):
        print("i am walk")

class dog:
    def swim(self):
        print("i am dog")
    def walk(self):
        print("i am dog walk")


def dktype(obj):
    obj.swim()
    obj.walk()
        

d = duck()
dg = dog()

dktype(d)