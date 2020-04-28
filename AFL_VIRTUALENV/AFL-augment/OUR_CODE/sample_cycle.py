class Sample:
    def __init__(self,function=None):
        self.function = function

    def test(self):
        i = 5

        for x in range(5,10):
            print(x)
        for y in range(15):
            print(y)
        for z in range(20,30,5):
            print(z)
        if x == 5 and y == 10 and y == 5:
            print(y)
            if z == 10:
                print(z)
