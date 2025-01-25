import datetime

# Classe Extrato
class Extrato:
    def __init__(self):
        self.transacoes = []  # Lista para armazenar as transações

    def exibir_extrato(self, numeroConta):
        print(f"Extrato da Conta {numeroConta}: \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")

# Classe Conta
class Conta:
    def __init__(self, clientes, numero, saldo):
        self.numero = numero
        self.clientes = clientes
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()

    def deposita(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transferenciaValor(self, contaDestino, valor):
        if self.saldo < valor:
            return "Não tem saldo"
        else:
            contaDestino.deposita(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, "Data", datetime.datetime.today()])
            return "Transferência concluída"

    def gerarsaldo(self):
        print(f"Numero: {self.numero} \nSaldo: {self.saldo}")

    def gerar_extrato(self):
        self.extrato.exibir_extrato(self.numero)  # Chama o método de extrato da classe Extrato

def main():
    c1 = Conta("Anderson", 1, 1000)
    print(f"Nome do titular da conta: {c1.clientes}")
    print(f"Número da conta: {c1.numero}")
    print(f"Saldo da conta: {c1.saldo}")

    c1.deposita(500)
    c1.sacar(150)
    c1.gerar_extrato()  # Exibe o extrato com as transações

    c2 = Conta("João", 2, 1500)
    print(f"\nTransferindo para a conta do {c2.clientes}...")
    c1.transferenciaValor(c2, 200)
    c2.gerar_extrato()  # Exibe o extrato da conta 2

if __name__ == "__main__":
    main()