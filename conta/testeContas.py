from cliente import Cliente
from Conta import Conta
from extrato import Extrato


clienteA = Cliente(312312,"Anderson","rua1")
clienteB = Cliente(242424,"Vapo","av paulista rua de Gay")

contaA = Conta([clienteA,clienteB],1,2000)
# contaA.gerarsaldo()
contaA.deposita(1400)
contaA.sacar(500)
contaA.saldo = -200
# contaA.gerarsaldo()
contaA.gerar_extrato()

contaB = Conta(clienteB,1,200)

contaB.deposita(23840)
contaB.sacar(10)

contaB.gerar_extrato()