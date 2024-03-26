print('Digite a sua idade')
anos = int(input('Digite quantos anos você tem: '))
meses = int(input('Digite quantos meses você completou após seu último aniversário: '))
while True:
    if meses < 0 or meses > 12:
        print('Digite um valor válido!')
        meses = int(input('Digite quantos meses você tem: '))

    else:
        break
dias = dias = int(input('Digite quantos dias você completou após o último mês completo: '))
while True:
    if dias < 0 or dias > 30:
        print('Digite um valor válido!')
        dias = int(input('Digite quantos dias você completou após o último mês completo: '))
    else:
        break

idade_em_dias = (anos * 365) + (meses * 30) + dias
print(f'Você tem {idade_em_dias} dias de idade')