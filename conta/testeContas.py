from cliente import Cliente
from Conta import Conta
from extrato import Extrato
from contaEspecial import ContaEspecial
from contaPoupanca import ContaPoupanca
from contaRemunerada import ContaRemuneradaPoupanca


clienteA = Cliente(312312,"Anderson","rua1")
clienteB = Cliente(242424,"Vapo","av paulista rua de Gay")
# clienteC = Cliente("789" ,"Joana", "Rua H")

contaA = Conta([clienteA,clienteB],1,5000)
# contaA.gerarsaldo()
contaApoupanca = ContaPoupanca(0.2)
contaAremunerada = ContaRemuneradaPoupanca(0.4,clienteA,5,23500)
contaAremunerada.remuneracaoConta()
contaAremunerada.gerarsaldo()
# contaA.deposita(1400)
# contaA.sacar(500)
# contaA.saldo = -200
# # contaA.gerarsaldo()
# contaA.gerar_extrato()

# contaB = Conta(clienteB,1,200)

# contaB.deposita(23840)
# contaB.sacar(10)

# contaB.gerar_extrato()

# contac = ContaEspecial([clienteC],3,1000,200)
# contac.deposita(100)
# contac.sacar(3200)
# contac.extrato.exibir_extrato(contac.numero)

# contac.gerar_extrato()



