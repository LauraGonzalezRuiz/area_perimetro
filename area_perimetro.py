import math
class Figura():
    def calculo_area(self):
        print('Esta figura no tiene área')
    def caluculo_perimetro(self):
        print('Esta figura no tiene perímetro')

class Cuadrado(Figura):
    def __init_(self,lado):
        self.lado=lado
    def caluculo_area(self):
        return self.lado * self.lado
    def calculo_perimetro(self):
        return 4 * self.lado

class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio
    def calculo_area(self):
        return math.pi*(self.radio**2)
    def calculo_perimetro(self)
        return 2*math.pi*self.radio

c=Cuadrado(2)
print(c.calculo_perimetro())

r = Circulo(2)
print(r.calculo_area())
