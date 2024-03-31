import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def a(self):
        return self.a

    def b(self):
        return self.b

    def c(self):
        return self.c

    def retangulo(self):
        if (self.a != self.b and self.a != self.c and self.b != self.c):
            if(self.a > self.b and self.a > self.c):
                if (self.a == math.sqrt((pow(self.b,2)+pow(self.c,2)))):
                    return True
            elif(self.b > self.c):
                if (self.b == math.sqrt((pow(self.a,2)+pow(self.c,2)))):
                    return True
            else:
                if (self.c == math.sqrt((pow(self.a,2)+pow(self.b,2)))):
                    return True
        return False
