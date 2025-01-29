from threading import Thread, Lock
from multiprocessing import Process

import time

minha_lista = []
tarefas = [] 
#array precisa ficar fora do main     
def funcao(indice):
    for i in range(10000):
        minha_lista.append(1)
        print('Minha Thread' , indice)

def main():
    for indice in range(10):
        tarefa = Thread(target=funcao,args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()
    print("Antes de aguardar o Termino!", len(minha_lista))
      
    for tarefa in tarefas:
         tarefa.join()
    print("Depois que rodar minha termino!" , len(minha_lista))

if __name__ == '__main__':
    main()