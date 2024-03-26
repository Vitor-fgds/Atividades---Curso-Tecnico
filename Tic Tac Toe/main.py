from tabuleiro import Tabuleiro, Jogador, Jogadas

tabuleiro = Tabuleiro()
jogador1 = Jogador('Vitor', 1)
jogador2 = Jogador('Júlia', 2)
numero_jogadas = Jogadas()

while True:
  print('Jogador 1')
  linha = int(input('Digite a linha da sua jogada (0-2): '))
  coluna = int(input('Digite a coluna da sua jogada (0-2): '))
  jogador1.fazer_jogada(tabuleiro, linha, coluna)
  tabuleiro.imprimir_tabuleiro()
  numero_jogadas.contar_jogada()
  
  if tabuleiro.verificar_vencedor(1):
        print("Jogador 1 venceu!")
        break
  elif numero_jogadas.verificar_empate():
      print("Empate!")
      break
  
  print("Jogador 2: ")
  linha = int(input("Digite a linha da sua jogada (0-2): "))
  coluna = int(input("Digite a coluna da sua jogada (0-2): "))
  jogador2.fazer_jogada(tabuleiro, linha, coluna)
  tabuleiro.imprimir_tabuleiro()
  numero_jogadas.contar_jogada()
  if tabuleiro.verificar_vencedor(2):
      print("Jogador 2 venceu!")
      break
  elif numero_jogadas.verificar_empate():
      print("Empate!")
      break