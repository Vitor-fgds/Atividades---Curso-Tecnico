senha_correta = 6789
senha = int(input('Digite uma senha de quatro números inteiros: '))
senha_str = str(senha)

               
while True:
  if len(senha_str) < 4 or len(senha_str) > 4:
    print('A senha deve ter quatro números inteiros')
    senha = int(input('Digite uma senha de quatro números inteiros: '))
    senha_str = str(senha)
  else:
    break

if senha == 6789:
  print('Senha correta, acesso garantido')
elif senha != 6789:
  print('Senha incorreta, acesso negado')
