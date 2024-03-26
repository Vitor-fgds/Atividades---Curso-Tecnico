print('Digite as notas!')
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
nota3 = float(input('Digite a nota da terceira prova: '))
texto_bonitinho = '''---------------------------------------------
1 - Média Aritmética
2 - Média Ponderada
3 - Média Harmônica
---------------------------------------------'''
print(texto_bonitinho)
opcao = int(input('Digite qual média você deseja: '))
while True:
  if opcao < 1 or opcao > 3:
    print('Digite uma opção válida!')
    opcao = int(input('Digite qual média você deseja: '))
  else:
    break
if opcao == 1:
  media_aritmética = (nota1 + nota2 + nota3) / 3
  print(f'Sua média aritmética é {media_aritmética:.2}')

elif opcao == 2:
    media_ponderada = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4))/ 10
    print(f'Sua média ponderada é: {media_ponderada:.2}')

elif opcao == 3:
  media_harmonica = 3 / ((1 / nota1) + (1 / nota2) + (1 / nota3))
  print(f'Sua média harmônica é: {media_harmonica:.2}')