import numpy as np
import matplotlib.pyplot as plt

#Questão 1 - Latência de uma plataforma digital

d = 1 # coloque seu último dígito (se for 0, use 10)

inicio = 0
fim = 6

x = np.linspace(inicio, fim, 300)
y = 180 + 45*np.cos((2*np.pi/3)*x)

x_ponto = 3
y_ponto = 180 + 45*np.cos((2*np.pi/3)*x_ponto)

plt.figure(figsize=(10, 4.5))
plt.plot(x, y)
plt.scatter([x_ponto], [y_ponto], label="t = 3")
plt.xlabel("Tempo (horas)")
plt.ylabel("Latência (ms)")
plt.title("Questão 1 - Latência - Matheus Sato - Rm569392")
plt.grid(True)
plt.legend()
plt.show()