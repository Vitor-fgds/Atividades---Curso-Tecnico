'''04) Crie uma classe chamada FiguraGeometrica com um método chamado calcular_area(). Em seguida, crie classes para representar diferentes tipos de figuras geométricas, como Retangulo, Circulo e Triangulo, que herdem da classe FiguraGeometrica. Implemente o método calcular_area() em cada classe para calcular e retornar a área correta da figura geométrica. Adicione atributos adicionais relevantes para cada classe, como base e altura para o Retangulo, raio para o Circulo e base e altura para o Triangulo.'''



class FiguraGeometrica:
  def __init__(self):
    pass

  def calcular_area():
    return True

class Quadrado(FiguraGeometrica):
  def __init__(self, lado):
    super().__init__()
    self._lado = lado

  def calcular_area(self):
    return self._lado * self._lado

class Retangulo(FiguraGeometrica):
  def __init__(self, base, altura):
    super().__init__()
    self._base = base
    self._altura = altura

  def calcular_area(self):
    return self._base * self._altura

class Triangulo(FiguraGeometrica):
  def __init__(self, base, altura):
    super().__init__()
    self._base = base
    self._altura = altura
    
  def calcular_area(self):
    return (self._base * self._altura) / 2

class Circulo(FiguraGeometrica):
  def __init__(self, raio, pi = 3):
    super().__init__()
    self._raio = raio
    self._pi = pi

  def calcular_area(self):
    return self._pi * (self._raio * self._raio)