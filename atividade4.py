import os
lista = list()
while True: 
    print('Inserir [I] - Editar [E] - Listar [L] - Remover [R]')
    escolha = input('Digite o que deseja fazer: ').upper()

    if escolha == 'I':       
        print("\n" * os.get_terminal_size().lines)
        item = input('Digite o item que deseja inserir: ')
        lista.append(item)
    elif escolha == 'E':    
        print("\n" * os.get_terminal_size().lines)   
        print(lista)
        alterar = int(input('Qual numero da posição do item que deseja alterar? '))
        lista[alterar] = input('Novo produto: ')
    elif escolha == 'L':  
        print("\n" * os.get_terminal_size().lines)     
        print(lista)
    elif escolha == 'R':
        print("\n" * os.get_terminal_size().lines)
        print(lista)
        remover = input('Qual item deseja remover: ')
        lista.remove(remover)
    elif escolha == '0':
        break
print("\n" * os.get_terminal_size().lines)
print(lista)