nome = input('digite seu nome: ')
sobrenome = input('Seu sobrenome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso:'))

print(nome, sobrenome, idade, peso)

if idade >=18:
    print('Maior de idade')
else:
    print('Menor de idade')