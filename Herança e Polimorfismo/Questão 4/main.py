from classes import Triangulo, Circulo, Retangulo, Quadrado

triangulo = Triangulo(8, 10)
print(triangulo.calcular_area())

retangulo = Retangulo(8, 10)
print(retangulo.calcular_area())

circulo = Circulo(4, 3)
print(circulo.calcular_area())

quadrado = Quadrado(8)
print(quadrado.calcular_area())