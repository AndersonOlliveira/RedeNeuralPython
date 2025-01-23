from Conta import Conta

Conta1 = Conta(1,123,'Leticia',0)
Conta2 = Conta(5,13423,'Vapo',0)

# print(f"{Conta2.nomeTitular}")\
    
# if Conta1 != Conta2:
#     print("sáo diferentes")
# else:
#     print('sao iguais')
# vou depositar

Conta1.deposita(1000)
Conta1.transferenciaValor(Conta2,500)
print(f"{Conta1.saldo} : minha conta 1 tem o x valor")
print(Conta2.saldo)
