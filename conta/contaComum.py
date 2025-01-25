from contaPoupanca import contaCliente

class ContaComum(contaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxarendimento)
        
    def CalculoRendimento(self):
       self.valorInvestido += (self.valorInvestido * self.taxarendimento)