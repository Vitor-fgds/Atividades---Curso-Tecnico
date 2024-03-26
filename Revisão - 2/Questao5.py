lista_idade = []
for i in range(1,21):
  x = int(input(f'Digite a {i}º idade: '))
  lista_idade.append(x)

print(45*'=')
print(f'A maior idade digitada é {max(lista_idade)} ano(s)!')
print(f'A menor idade digitada é {min(lista_idade)} ano(s)!')
print(45*'=')
