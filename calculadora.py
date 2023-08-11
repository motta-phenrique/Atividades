print('Calculadora em Python')
print('___'* 30)

op = 10

while op != 0:
    print('Qual operacao deseja: [+] - Soma / [*] - Multiplicacao / [-] - Subtracao / [/] - Divisao / [S] - Sair')
    
    op = input()
    if op == 'S':
        break

    n1 = int(input('Digite o Primeiro Numero: '))
    n2 = int(input('Digite o Segundo Numero: '))


    if op == 1:
        soma = n1 + n2
        print(soma)
    elif op == 2:
        mult = n1 * n2
        print(mult)
    elif op == 3:
        sub = n1 - n2
        print(sub)
    elif op == 4:
        div = n1 / n2
        print(div)


