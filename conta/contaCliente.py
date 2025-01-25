from contaPoupanca import contaCliente

class ContaRemunerada(contaCliente):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
       super().__init__(numero,IOF,IR,valorinvestido,taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido -= self.valorinvestido * self.IOF