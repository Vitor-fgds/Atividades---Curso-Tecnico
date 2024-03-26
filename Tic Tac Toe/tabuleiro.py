import numpy as np

class Tabuleiro:
  def __init__(self):
    self.tabuleiro = np.zeros((3,3), dtype = int)


  def imprimir_tabuleiro(self):
     for x in range(3):
            for y in range(3):
                if self.tabuleiro[x][y] == 0:
                    print("|_|", end=" ")
                elif self.tabuleiro[x][y] == 1:
                    print("|X|", end=" ")
                else:
                    print("|O|", end=" ")
            print()
       
  def verificar_vencedor(self, jogador):
        for x in range(3):
            # Verificar se há três em uma linha
            if self.tabuleiro[x][0] == jogador and self.tabuleiro[x][1] == jogador and self.tabuleiro[x][2] == jogador:
                return True
            # Verificar se há três em uma coluna
            elif self.tabuleiro[0][x] == jogador and self.tabuleiro[1][x] == jogador and self.tabuleiro[2][x] == jogador:
                return True
        
        # Verificar se há três em uma diagonal
        if self.tabuleiro[0][0] == jogador and self.tabuleiro[1][1] == jogador and self.tabuleiro[2][2] == jogador:
            return True
        elif self.tabuleiro[0][2] == jogador and self.tabuleiro[1][1] == jogador and self.tabuleiro[2][0] == jogador:
            return True
        
        return False

class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo
        
    def fazer_jogada(self, tabuleiro, linha, coluna):
        tabuleiro.tabuleiro[linha][coluna] = self.simbolo
      
class Jogadas:
    def __init__(self):
        self.jogadas = 0
        
    def contar_jogada(self):
        self.jogadas += 1
        
    def verificar_empate(self):
        if self.jogadas == 9:
            return True
        else:
            return False
  