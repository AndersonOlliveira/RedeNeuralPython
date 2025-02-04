from subprocess import Popen
from os import listdir

def cria_dir(diretorio): 
    dir = Popen(["hdfs", "dfs", "-mkdir",diretorio])
    dir.wait()
def move_arqs(arquivo,diretorio):
    Popen(["hdfs","dfs","-put", arquivo,diretorio])
    cria_dir("dados1901JSON")
    arquivos = list(filter(lambda x: x.endswith(".json"), listdir("./")))
    for arquivo in arquivos:
        move_arqs(arquivo,"dados1901JSON")