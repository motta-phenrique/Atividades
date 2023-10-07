class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Valor inválido')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def verSaldo(self):
        print(f'Saldo = R${self.saldo}')


conta1 = ContaBancaria("Paulo", 0)


conta1.depositar(700)
conta1.sacar(70)
conta1.verSaldo()
