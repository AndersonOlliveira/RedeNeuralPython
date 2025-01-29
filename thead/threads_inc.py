from threading import Thread,Lock
from multiprocessing import Process
import time

contador = 0 
tarefas = []

def funcao(indice):
    global contador
    for i in range(10000):
        contador += 1
        print("Termino Thread", indice)
        
def main():
    for indice in range(10): 
     tarefa = Thread(target=funcao,args=(indice,))
     tarefas.append(tarefa)
     tarefa.start()
print('Äntes de Aguardar o Terminio', contador)
    
for tarefa in tarefas:
   tarefa.join()
print("Após aguardar o termino", contador)
        
if __name__ == '__main__':
    main()
    