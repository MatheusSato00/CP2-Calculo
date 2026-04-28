import numpy as np
import matplotlib.pyplot as plt

#Questão 3 - Temperatura de um servidor ao longo do dia

#último dígito da matrícula
d = 1  

#intervalo de horas
inicio = 0
fim = 24

#eixo x
x = np.linspace(inicio, fim, 300)

#função da temperatura
y = 70 + 15*np.sin((np.pi/6)*(x - 3))

#ponto específico
x_ponto = 6
y_ponto = 70 + 15*np.sin((np.pi/6)*(x_ponto - 3))

#gráfico
plt.figure(figsize=(10, 4.5))
plt.plot(x, y, label="Temperatura T(h)")
plt.scatter([x_ponto], [y_ponto], color='red', label="h = 6")
plt.xlabel("Hora do dia")
plt.ylabel("Temperatura (°C)")
plt.title("Questão 3 - Temperatura do Servidor - Matheus Sato - Rm569392")
plt.grid(True)
plt.legend()
plt.show()