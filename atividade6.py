alunos = dict()
escola = list()
soma = 0


for i in range(0, 3):
    alunos['nome'] = input(f'Digite o nome do aluno {i+1}: ')
    alunos['nota1'] = int(input(f'Digite a primeira nota do aluno {i+1}: '))
    alunos['nota2'] = int(input(f'Digite a segunda nota do aluno {i+1}: '))
    escola.append(alunos.copy())

for a in escola:
    for i, j in a.items():
        if i == 'nota1' or i == 'nota2':
            soma += j

print(f'A soma das notas é = {soma}')