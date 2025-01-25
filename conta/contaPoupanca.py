import datetime

class ContaPoupanca:
    def __init__(self,taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()
        
    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao

class contaCliente:
    def __init__(self,numero, IOF,IR,valorInvestido,taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR  = IR
        self.valorInvestido = valorInvestido
        self.taxarendimento = taxarendimento
        
    def CalculoRendimento(self):
        self.valorInvestido += (self.valorInvestido * self.taxarendimento)
        self.valorInvestido = (self.valorInvestido -(self.valorInvestido * self.IOF * self.IR))
     
    def ExtratoRendimento(self):
       print(f"O saldo atual da conta e {self.numero} é {self.valorInvestido:10.2f}")        
        