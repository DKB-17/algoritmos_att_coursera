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

    def semelhantes(self, triangulo):
        if((self.a/triangulo.a) == (self.b/triangulo.b) and (self.a/triangulo.a) == (self.c/triangulo.c) ):
            return True
        return False
    