import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#utilizar este sys path, para caminho de pasta, niveis
from circulo import Circulo

cirA = Circulo(2,10,5)
cirA.total_circulo
print(cirA.total_circulo)
print(Circulo.total_circulo)