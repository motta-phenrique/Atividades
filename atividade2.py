altura = float(input('Digite sua altura: '))
peso = int(input('Digite seu peso:'))

imc = peso / (altura ** 2)

print(f'Seu imc eh {imc:.2f}')
