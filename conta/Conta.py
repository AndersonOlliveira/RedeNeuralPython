
import datetime
from extrato import Extrato
class Conta:
    # pass
# A palavra reservada pass, por sua vez, indica que a classe será definida posteriormente
#  __init__ como o construtor da classe
  def __init__(self,clientes,numero,saldo):
      self.numero = numero
      self.clientes = clientes
    #   self.nomeTitular = nomeTitular
      self.saldo = saldo
      self.dataabertura = datetime.datetime.today()
      self.extrato = Extrato() 
  def deposita(self, valor):
    self.saldo += valor
    self.extrato.transacoes.append(["DEPOSITO", valor, "Data",datetime.datetime.today()])

  def sacar(self,valor):
    if self.saldo < valor:
        return False
    else:
      self.saldo -= valor
      self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) 
           
      return True
  def transferenciaValor(self,contaDestino,valor):
       if self.saldo < valor:
        return ("Não tem Saldo")
       else:
        contaDestino.deposita(valor)
        self.saldo -= valor
        self.Extrato.transacoes.append(["TRANSFERENCIA REALIXA COM SUCESSO",valor, 'Data', datetime.datetime.today()])
        return('Transferencia Concluida')
  def gerarsaldo(self):
        print(f"numero:{self.numero} \n saldo: {self.saldo}")      
       
    
  def gerar_extrato(self):
    print(f"numero :{self.numero } \n cpf: {self.cpf}\nsaldo: {self.saldo}")
    
      
def main():
    # c1 = Conta(1,'420.044.555.20','Anderson', 1000)
    # # print (f"Nome do titular da conta: {c1.nomeTitular}")
    # print (f"Número da conta: {c1.numero}")
    # # print (f"CPF do titular da conta: {c1.cpf}")
    # print (f"Saldo da conta: {c1.saldo}")
    # c1.deposita(500)
    # c1.sacar(150)
    # c1.gerar_extrato()
    
    
 if __name__ == "__main__":
    main()
    
# class A():
#     def f(self):
#         print("foo")


# def main():
#     obj_A = A() # Objeto sendo instanciado
#     obj_A.f()

# if __name__ == "__main__": 
#     main()

