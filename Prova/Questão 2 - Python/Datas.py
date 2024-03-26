class Datas:
  def __init__(self, dia, mes, ano):
    if dia > 0 and dia < 31:
      self._dia = dia
    else:
      print(f'Dia Inválido')
      exit
      
    if mes > 0 and mes < 13:
      self._mes = mes
    else:
      print(f'Mês Inválido')
      exit

    if ano >= 0:
      self._ano = ano

    else:
      print(f'Ano Inválido')
      exit

  @property
  def dia(self):
    return self._dia
      
  @dia.setter
  def dia(self, novo_dia):
    if novo_dia > 0 and novo_dia < 31:
      self._dia = novo_dia
    else:
      print(f'Dia Inválido')
      return False

  @property
  def mes(self):
    return self._mes

  @mes.setter
  def mes(self,novo_mes):
    if novo_mes > 0 and novo_mes < 13:
       self._mes = novo_mes
    else:
      print(f'Mês Inválido')
      return False

  @property
  def ano(self):
    return self._ano

  @ano.setter
  def ano(self, novo_ano):
    if novo_ano >= 0:
      self._ano = novo_ano
    else:
      print(f'Ano Inválido')
      return False

  def toString(self):
    return (f'{self._dia}/{self._mes}/{self._ano}')

  def avançar_dia(self):
    if self._dia < 30:
      self._dia +=1
    elif self._dia == 30 and self._mes < 12:
      self._dia = 1
      self._mes += 1
    elif self._dia == 30 and self._mes == 12:
      self._dia = 1
      self._mes = 1
      self._ano += 1
    
  def data_menor(self,data1,data2):
    if data1.ano < data2.ano:
      print("Data 1 é menor")
      return True
    elif data1.ano > data2.ano:
      print("Data 2 é menor")
      return False
    elif data1.ano == data2.ano and data1.mes < data2.mes:
      print("Data 1 é menor")
      return True
    elif data1.ano == data2.ano and data1.mes > data2.mes:
      print("Data 2 é menor")
      return False
    elif data1.ano == data2.ano and data1.mes > data2.mes and data1.dia < data2.dia:
      print("Data 1 é menor")
      return True
    elif data1.ano == data2.ano and data1.mes > data2.mes and data1.dia > data2.dia:
      print("Data 2 é menor")
      return False
    