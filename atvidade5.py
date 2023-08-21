lista = list()
soma = 0
for i in range(0, 5):
    num = int(input('digite um numero: '))
    lista.append(num)

for i, item in enumerate(lista):
    soma += lista[i]

print(lista)
print(f'soma de todos os elemntos da lista é: {soma}')