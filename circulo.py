class Circulo():
    #controlando a quantidade de cirulos
    _total_circulo = 0
    
    def __init__(self,pontox,pontoy,raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulo +=1
        
        
    @classmethod
    def get_total_circulo(cls):
        return cls._total_circulo