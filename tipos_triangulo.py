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

    def perimetro(self):
        return (self.a+self.b+self.c)

    def tipo_lado(self):
        if self.a == self.b:
            if self.a == self.c:
                return "equilátero"
            else:
                return "isósceles"
        elif self.a == self.c:
            return "isósceles"
        elif self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"
