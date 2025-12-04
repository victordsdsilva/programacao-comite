class conta:
    #Atributos
    def __init__(self, saldo):
        self.saldo = int(saldo)

    # Metodos
    def depositar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} | ')
        self.saldo += valor
        print(f'Saldo atual | {self.saldo} | ')


    def sacar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} | ')
        self.saldo -= valor
        print(f'Saldo atual | {self.saldo} | ')


    def main():
        minha_conta = conta(3000)
        minha_conta.sacar(int(input('informe valor do saque -> ')))
        print()
        minha_conta.depositar(int(input('informe valor do deposito -> ')))

    main()    