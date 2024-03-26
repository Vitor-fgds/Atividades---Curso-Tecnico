'''03) Crie uma classe chamada Animal com um método chamado emitir_som(). Em seguida, crie classes para representar diferentes tipos de animais, como Cachorro, Gato e Passaro, que herdem da classe Animal. Implemente o método emitir_som() em cada classe para exibir o som característico do animal. Adicione atributos adicionais relevantes para cada classe, como raca para o Cachorro, cor para o Gato e tamanho para o Passaro. Reescreva o método __str__() em cada classe filha para retornar uma representação adequada do objeto em questão.'''

from classes import Cachorro, Gato, Passaro

cachorro = Cachorro("Beagle", 18) 
print(cachorro.emitir_som())
cachorro.__str__()

gato = Gato("Preto", 18)
print(gato.emitir_som())
gato.__str__()

passaro = Passaro("Pequeno", 18)
print(passaro.emitir_som())
print(passaro.__str__())