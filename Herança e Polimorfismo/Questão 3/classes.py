'''03) Crie uma classe chamada Animal com um método chamado emitir_som(). Em seguida, crie classes para representar diferentes tipos de animais, como Cachorro, Gato e Passaro, que herdem da classe Animal. Implemente o método emitir_som() em cada classe para exibir o som característico do animal. Adicione atributos adicionais relevantes para cada classe, como raca para o Cachorro, cor para o Gato e tamanho para o Passaro. Reescreva o método __str__() em cada classe filha para retornar uma representação adequada do objeto em questão.'''

class Animal:
  def __init__(self, idade):
    self._idade = idade

  def emitir_som(self):
    return f'(....)'

class Cachorro(Animal):
  def __init__(self,raca,idade):
    super().__init__(idade)
    self._raca = raca
    
  def emitir_som(self):
    return f'Au Au'

  def __str__(self):
    return f'{self.__class__.__name__} \nRaça: {self._raca} \nSom: Au Au \nIdade: {self._idade}'

class Passaro(Animal):
  def __init__(self,tamanho,idade):
    super().__init__(idade)
    self._tamanho = tamanho
    
  def emitir_som(self):
    return f'Piu Piu'
    
  def __str__(self):
    return f'{self.__class__.__name__} \nTamanho: {self._tamanho} \nSom: Piu Piu \nIdade: {self._idade}'

class Gato(Animal):
  def __init__(self,cor,idade):
    super().__init__(idade)
    self._cor = cor
    

  def emitir_som(self):
    return "Miau"
    
  def __str__(self):
    return f'{self.__class__.__name__} \nCor: {self._cor} \nSom: Miau \n Idade: {self._idade}'
    
