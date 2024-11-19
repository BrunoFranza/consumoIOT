# Importar bibliotecas necessárias
import time
import random  # Para simulação de dados reais de sensores
import matplotlib.pyplot as plt
import pandas as pd

# Função para simular a leitura de um sensor de consumo de energia
def ler_sensor_energia():
    # Simula o consumo em kWh
    return round(random.uniform(10.0, 100.0), 2)

# Lista para armazenar os dados de consumo
dados_consumo = []
timestamps = []

# Coleta de dados em um intervalo de 10 minutos (simulado)
for i in range(10):
    consumo = ler_sensor_energia()
    timestamp = pd.Timestamp.now()

    dados_consumo.append(consumo)
    timestamps.append(timestamp)

    print(f"{timestamp}: Consumo de energia: {consumo} kWh")

    # Simula um intervalo de 1 segundo entre as leituras para teste
    time.sleep(1)

# Criar um DataFrame para facilitar a análise
df_consumo = pd.DataFrame({
    'Timestamp': timestamps,
    'Consumo (kWh)': dados_consumo
})

# Plotar os dados coletados
plt.figure(figsize=(10, 5))
plt.plot(df_consumo['Timestamp'], df_consumo['Consumo (kWh)'], marker='o', linestyle='-', color='b')
plt.title('Monitoramento de Consumo de Energia em Tempo Real')
plt.xlabel('Horário')
plt.ylabel('Consumo (kWh)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Salvando os dados em um arquivo CSV para análise futura
df_consumo.to_csv('consumo_energia.csv', index=False)
