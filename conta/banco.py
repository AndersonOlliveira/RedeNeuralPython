from Conta import Conta
from cliente import Cliente
from extrato import Extrato
from contaPoupanca import contaCliente
from contaComum import ContaComum
from contaRemunerada import ContaRemuneradaPoupanca

class Banco():
    def __init__(self, codigo,nome):
      self.codigo = codigo
      self.nome = nome
      self.contas = []
      
    def adicionarConta(self,contaCliente):
        self.contas.append(contaCliente)
    
    def calcularendimentomensal(self):
        for c in self.contas:
            c.CalculoRendimento()
        
    def imprimesaldocontas(self):
      for c in self.contas:
          return c
      

banco1 = Banco(999,"teste")
contacliente1 = contaCliente (1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemuneradaPoupanca(3,0.01,0.1,2000)

banco1.adicionarConta(contacliente1) #(4)
banco1.adicionarConta(contacomum1) #(5)
banco1.adicionarConta(contaremunerada1) #(6)
banco1.calcularendimentomensal#(7)
banco1.imprimesaldocontas() #(8)