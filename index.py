import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
minimo = 20
maximo = 40
qtd_pontos = 100
np.random.seed(1234)
y = np.random.uniform(minimo, maximo, qtd_pontos)
x = np.arange (1,qtd_pontos+1,1)

plt.title('Série Temporal')
plt.xlabel('Período')
plt.ylabel('Valor')
plt.plot(x,y)
# plt.show()

minimo = np.min(y)
maximo - np.max(y)
y = (y- minimo)/(maximo - minimo)


percentual_treinamento = 0.8
qtd_treinamento = int(percentual_treinamento*(len(x)))

x_treino = x[0:qtd_treinamento]
x_teste = x[qtd_treinamento:]

y_treino = y[0:qtd_treinamento]
y_teste = y[qtd_treinamento:]

treino = np.array(list(zip(x_treino, y_treino)))

teste = np.array(list(zip(x_teste, y_teste)))

for i in range(5):
    print('Treino[{}]: {}'.format(i+1, treino[i]))
    

def preparar_dados(dados_serie, look_back):
    X, y = [],[]
    n = len(dados_serie)
    for i in range(n - look_back):
        posicao_fim = i + look_back
        if posicao_fim <= n:
            seg_x = dados_serie[i:posicao_fim,1]
            seg_y = dados_serie[posicao_fim,1]
            X.append(seg_x)
            y.append(seg_y)

    return np.array(X), np.array(y)

look_back = 2
x_treino, y_treino = preparar_dados(treino, look_back)
x_teste, y_teste = preparar_dados(teste, look_back)
 
n_caracteristicas = 1 
x_treino = x_treino.reshape((x_treino.shape[0], x_treino.shape[1], n_caracteristicas))
x_teste = x_teste.reshape((x_teste.shape[0], x_teste.shape[1], n_caracteristicas))
    

for i in range(5):
    print('treino[{}]: {} -> {}'.format(i+1,x_treino[i], y_treino[i]))

n_etapas = x_treino.shape[1]
n_caracteristicas = x_treino.shape[2]
n_unidades = 100
tf.random.set_seed(8888) # Setting seed to ensure reproducibility.
modelo = Sequential()
camada_de_entrada=(n_etapas, n_caracteristicas)
modelo.add(LSTM(n_unidades, return_sequences = True, input_shape = camada_de_entrada))
modelo.add(Dropout(0.2))
modelo.add(LSTM(128, input_shape = camada_de_entrada))
modelo.add(Dense(1))

modelo.summary()

modelo.compile(loss = 'mean_squared_error', optimizer = 'adam')


epocas = 20
historico = modelo.fit(x_treino, y_treino, epochs = epocas, batch_size = 70, verbose = 2, shuffle = False,validation_split = 0.3)


hist = pd.DataFrame(historico.history)
hist.head()

modelo.save_weights('Meu_Modelo_LSTM.weights.h5')
loss = modelo.evaluate(x_teste, y_teste, batch_size=64)
print('loss: {}'.format(loss))
plt.title('Cálculo do Erro ao longo do treinamento')
plt.ylabel('Erro')
plt.xlabel('Época')
plt.plot(historico.history['loss'])
plt.plot(historico.history['val_loss'])
plt.legend(['loss (treinamento)', 'val_loss (validação)'], loc='upper right')
plt.show()
modelo.load_weights('Meu_Modelo_LSTM.weights.h5')
predicao = modelo.predict(x_teste)
valores_reais_y = y_teste
plt.figure(figsize=(50,10))
plt.plot(list(range(len(valores_reais_y))),valores_reais_y, marker='.', label='Real')
lst_dados_predicao=[w[0] for w in predicao]
plt.plot(list(np.arange(len(predicao))-look_back), lst_dados_predicao,'r',label='Estimação do Modelo')
plt.ylabel('valores', size=15)
plt.xlabel('período', size=15)
plt.legend(fontsize=15)
plt.show()