from threading import Thread,Lock
from multiprocessing import Process
import time

startTime = time.time()
def funcao_a(nome):
    print(nome)
    for nomes in nome:
        print('meus nome' , nomes)

def funcaoA(indice):
    for indices in range(indice +10):
        print('Minha funcao A tem o valor de', indices)
    
    
def main():
    print("meu tempo e inicial" , startTime)
    t = Thread(target=funcao_a, args=('minha funcao',))
    t.start()
    time.sleep(2)
    t.join()
    
    a = Thread(target=funcaoA , args=(10,))
    a.start()
    time.sleep(3)
    a.join()
  
    endTime = time.time()
    print('TENHO PAUSA DE', endTime)
    elapsedTime = endTime - startTime
    print("Elapsed Time = %s" % elapsedTime)
    
    
    
if __name__ == '__main__':
    main()