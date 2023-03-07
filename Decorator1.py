def abc(fun):
    def xyz():
        print("HELLO")
        fun()
        print("HELLO")
        fun()
    return xyz
@abc
def deco():
    print("pqr")
deco()