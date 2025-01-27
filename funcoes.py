# valor = 20

# def multiplica(fator):
#     global valor
#     valor = valor * fator
#     print("Resultado", valor) 

# def main():
#     numero = int(input())
#     multiplica(numero)
#     multiplica(numero)
# valores = 20

# def multiplicacao(valor, fator):
#      valor = valor * fator
#      return valor
# def main():
#      numeros = int(input("digite o valor: "))
#      print("valor passado" , multiplicacao(valores,numeros))
#      print("Resultado", multiplicacao(valores, numeros))
 
#

# valores = input()
# valores =[int(i) for i in 
# valores.split()]

# def altera_lista(lista):
#     lista[2] = lista[2] + 10
#     return lista

# def main():
#     print("Nova Lista", altera_lista(valores))
#     print("Nova Lista 2", altera_lista(valores))
 
 
# valores = input()

# valores = [int(i) for i in valores.split()]

# def altera_lista(lista):
#     nova_lista = list(lista)
#     nova_lista[2] = nova_lista[2] + 10
#     return lista 
     
# def main():
#     print("Nova Lista", altera_lista(valores))
#     print("Nova Lista 2", altera_lista(valores))
    
 #Funções de ordem superior

# def multiplicar_por(multiplicador):
#     def multi(multiplicando):
#         return multiplicando * multiplicador
#     return multi
# def main():
#     multiplicar_por_10 = multiplicar_por(10)
#     print(multiplicar_por_10(4))
#     print(multiplicar_por_10(2))
#     multiplicar_por_5 = multiplicar_por(5)
#     print(multiplicar_por_5(1))
#     print(multiplicar_por_5(2))

#Funções lambda

# multiplicador = lambda x:10*x
# print(multiplicador(1))

# lista = [1,2,3,4,5]

# def triplica_itens(iterable):
#     lista_aux = []
#     for item in iterable:
#         lista_aux.append(item*3)
#         return lista_aux

# def main():
#     nova_lista = triplica_itens(lista)
#     print(nova_lista)
    
# nova_lista = filter(lambda item: item % 2 !=0, lista)
 
# def main():
#      print(list(nova_lista))


#execio 

veiculos = ['aviao', 'carro' ,'navio', 'ónibus']

f_ma = lambda x: str.upper(x)
nome = list(map(f_ma,veiculos))
print(f'lista = {nome}')
    

# if __name__ == "__main__":
#     main()   