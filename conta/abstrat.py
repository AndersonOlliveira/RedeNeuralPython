from abc import ABC, abstractmethod

class ContaCliente(ABC):
    def __init__(self,numero,IOF,IR,valorinvestido,taxarendimento):
        self.numero = numero
        self.IOF =   IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass
    
cc1 = ContaCliente(1,0.1,0.25,0.1)