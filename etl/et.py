import gzip
from os import listdir

def transformar(linha):
    data = linha[15:23].decode("utf8-8")
    hora = linha[23:27].decode("utf8-8")
    temperatura = int(linha[87:92])
    return "{\"data\":\""+data+"\", \"hora\":\""+hora+"\","+" \" temperatura:\":"+str(temperatura)+"}\n"

def ler(nomeArquivo):
    saida = "[ "
    with gzip.open(arquivo, "rb") as fin: 
        for linha in fin: 
            if saida!="[" : saida += ", "
            saida + "]"
            with open(nomeArquivo+".json", "w") as f:
                f.write(saida)
    arquivos = list(filter(lambda x: x.endswith(".gz"), listdir()))
    for arquivo in arquivos: ler(arquivo)
    