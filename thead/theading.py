from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)
    
def main():
    t = Thread(target=funcao_a, args=('minha funcao',))
    t.start()
    
    p = Process(target=funcao_a, args=('Meu processo',))
    p.start()
    
if __name__ == '__main__':
    main()