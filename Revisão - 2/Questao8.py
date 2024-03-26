import datetime
while True:
    print('--------------- CÁLCULO DE HORAS E DATA EM DIFERENTES LOCALIZAÇÕES ---------------')
    print('Desenvolvido por Vitor Moura - Estudante de TI do IFNMG\n')

    print('UTILIZE NÚMEROS INTEIROS PARA INFORMAR O HORÁRIO CONHECIDO')
    while True:
        horas = int(input('Digite as horas do local com horário conhecido:  '))
        if horas > 23 or horas < 0:
            print('DIGITE UM VALOR VÁLIDO!')
            horas = int(input('Digite as horas do local com horário conhecido:  '))
            if horas < 24 and horas >= 0:
                break
        else:
            break

    while True:
        minutos = int(input('Digite os minutos do local com horário conhecido:  '))
        if minutos > 59 or minutos < 0:
            print('DIGITE UM VALOR VÁLIDO!')
            minutos = int(input('Digite os minutos do local com horário conhecido:  '))
            if minutos < 60 and minutos >= 0:
                break
        else:
            break

    while True:
        dia = int(input('Digite o dia do local com horário conhecido:  '))
        if dia > 31 or dia <= 0:
            print('DIGITE UM VALOR VÁLIDO!')
            if dia < 32 and dia > 0:
                break
        else:
            break

    while True:
        mes = int(input('Digite o mês do local com horário conhecido: '))
        if mes > 12 or mes < 1:
            print('DIGITE UM VALOR VÁLIDO')
            mes = int(input('Digite o mês do local com horário conhecido: '))
            if mes < 13 and mes > 0:
                break
        else:
            break
    while True:
        ano = int(input('Digite o ano do local com horário conhecido: '))
        if ano < 0:
            print('DIGITE UM VALOR VÁLIDO')
            ano = int(input('Digite o ano do local com horário conhecido: '))
            if ano > 0:
             break
        else:
            break

    horario_cidade1 = datetime.datetime(ano, mes, dia, horas, minutos)



    while True:
        loc_cidade1 = str(input('Digite o hemisfério do local com horário conhecido (Leste ou Oeste): ')).upper()
        if loc_cidade1 != 'LESTE' and loc_cidade1 != 'OESTE':
            print('DIGITE UM HEMISFÉRIO VÁLIDO!')
            loc_cidade1 = str(input('Digite o hemisfério do local com horário conhecido (Leste ou Oeste): ')).upper()
            if loc_cidade1 == 'LESTE' or loc_cidade1 == 'OESTE':
                break

        else:
            break

    while True:
        loc_cidade2 = str(input('Digite o hemisfério do local com horário desconhecido (Leste ou Oeste): ')).upper()
        if loc_cidade2 != 'LESTE' and loc_cidade2 != 'OESTE':
            print('DIGITE UM HEMISFÉRIO VÁLIDO!')
            loc_cidade2 = str(input('Digite o hemisfério do local com horário desconhecido (Leste ou Oeste): ')).upper()
            if loc_cidade2 == 'LESTE' or loc_cidade2 == 'OESTE':
             break

        else:
            break
    while True:
        long_cidade1 = int(input('Digite a longitude do local com horário conhecido (Apenas números inteiros):  '))
        if long_cidade1 > 180 or long_cidade1 < 0:
            print('DIGITE UMA LONGITUDE VÁLIDA!')
            long_cidade1 = int(input('Digite a longitude do local com horário conhecido (Apenas números inteiros):  '))
            if long_cidade1 <= 180 and long_cidade1 >= 0:
                break

        else:
         break

    while True:
        long_cidade2 = int(input('Digite a Longitude do local com horário desconhecido (Apenas números inteiros):  '))
        if long_cidade2 > 180 or long_cidade2 < 0:
            print('DIGITE UMA LONGITUDE VÁLIDA!')
            long_cidade2 = int(input('Digite a Longitude do local com horário desconhecido (Apenas números inteiros):  '))
            if long_cidade2 <= 180 and long_cidade2 >= 0:
                break

        else:
            break

    long_calc = long_cidade1 + long_cidade2
    if loc_cidade1 == loc_cidade2:
        if long_cidade2 > long_cidade1:
         long_calc = long_cidade2 - long_cidade1
        elif long_cidade1 > long_cidade2:
            long_calc = long_cidade1 - long_cidade2
    dif_fuso = 0
    if long_calc % 15 == 0:
        dif_fuso = long_calc // 15
    elif long_calc % 15 != 0:
        dif_fuso = (long_calc // 15) + 1
      

    print(f'A diferença de Fusos Horários entre X e Y é de {dif_fuso} fusos\n')
  
  
    
   
    

    if loc_cidade1 == 'OESTE' and loc_cidade2 == 'LESTE':
        horario_2 = horario_cidade1 + datetime.timedelta(hours=dif_fuso)
        print(f'O horário desconhecido é {horario_2}')
    elif loc_cidade1 == 'OESTE' and loc_cidade2 == 'LESTE' and dif_fuso == 24:
        horario_2 = horario_cidade1 + datetime.timedelta(days=1)
        print(f'O horário desconhecido é {horario_2}')

    elif loc_cidade1 == 'LESTE' and loc_cidade2 == 'OESTE':
        horario_2 = horario_cidade1 - datetime.timedelta(hours=dif_fuso)
        print(f'O horário desconhecido é {horario_2}')
      
    elif loc_cidade1 == 'LESTE' and loc_cidade2 == 'OESTE' and dif_fuso == 24:
        horario_2 = horario_cidade1 - datetime.timedelta(days=1)
        print(f'O horário desconhecido é {horario_2}')
      
    elif loc_cidade1 == 'LESTE' and loc_cidade2 == 'LESTE':
        if long_cidade2 > long_cidade1:
            horario_2 = horario_cidade1 + datetime.timedelta(hours=dif_fuso)
            print(f'O horário desconhecido é {horario_2}')
        elif long_cidade1 > long_cidade2:
            horario_2 = horario_cidade1 - datetime.timedelta(hours=dif_fuso)
            print(f'O horário desconhecido é {horario_2}')
    elif loc_cidade1 == 'OESTE' and loc_cidade2 == 'OESTE':
        if long_cidade2 > long_cidade1:
            horario_2 = horario_cidade1 - datetime.timedelta(hours=dif_fuso)
            print(f'O horário desconhecido é {horario_2}')
        elif long_cidade1 > long_cidade2:
            horario_2 = horario_cidade1 + datetime.timedelta(hours=dif_fuso)
            print(f'O horário desconhecido é {horario_2}')
    print('--------------------------------------------------------------------------------------------------------------------')
    print('1 ---- CONTINUAR\n0 ---- FECHAR')
    x = (int(input('INSIRA UM VALOR (0 OU 1): ')))
    if x != 0 and x != 1:
        while True:
            print('DIGITE UM VALOR VÁLIDO')
            x = (int(input('INSIRA UM VALOR (0 OU 1): ')))
            if x == 0:
                exit()
            elif x == 1:
                break
            else:
                True

    elif x == 0:
        break
