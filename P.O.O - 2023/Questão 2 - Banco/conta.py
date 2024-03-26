import datetime
class Conta:
  def __init__(self, numero,cliente,saldo,limite, data):
    self.numero = numero
    self.titular = cliente
    self.saldo = saldo
    self.limite = limite
    self.data_abertura = data.data_atual
    
  def deposita(self,valor):
    self.saldo += valor
    
  def saca(self,valor):
    if self.saldo < valor:
      return False
    else:
      self.saldo -= valor

  def extrato(self,cliente,data):
    print(f'Número: {self.numero} \nCliente: {cliente.nome} {cliente.sobrenome} \nCPF: {cliente.cpf} \nSaldo: {self.saldo} \nData de Abertura: {data.data_atual}')

  def transfere_para(self,destino,valor):
    retirou = self.saca(valor)
    if retirou == False:
      return False
    else:
      destino.deposita(valor)
      return True

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
      self.nome = nome
      self.sobrenome = sobrenome
      self.cpf = cpf
class Data:
  def __init__(self,dia,mes,ano):
    self.dia = dia
    self.mes = mes
    self.ano = ano
    self.data_atual = datetime.date(self.ano,self.mes,self.dia)
  