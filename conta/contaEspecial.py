import datetime
from Conta import Conta
from cliente import Cliente
from extrato import Extrato


class ContaEspecial(Conta):
    def _init_(self,clientes,numero,saldo,limite):
        Conta. __init__(self,clientes,numero,saldo, limite)
        self.limite = limite
    
    def sacar(self,valor):
        if(self.saldo + self.limite) < valor:
            return False
        else:
         self.valor -= valor
         self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
         return True