import numpy as np
import matplotlib.pyplot as plt
 
 #Questão 2 - Fluxo de clientes em um supermercado

h = np.linspace(0, 24, 300)
N = 900 - 800*np.sin((np.pi/12)*h)
 
h_ponto = 2
N_ponto = 900 - 800*np.sin((np.pi/12)*h_ponto)
 
#pontos de máximo e mínimo
h_min = 6
N_min = 900 - 800*np.sin((np.pi/12)*h_min)
 
h_max = 18
N_max = 900 - 800*np.sin((np.pi/12)*h_max)
 
plt.figure(figsize=(10,4.5))
plt.plot(h, N)
plt.scatter([h_ponto], [N_ponto], color='red')
plt.scatter([h_min, h_max], [N_min, N_max], color='green')
plt.xlabel("Horário do dia (h)")
plt.ylabel("Número de clientes")
plt.title("Questão 2 - Fluxo de clientes - Matheus Sato - Rm569392")
plt.grid(True)
plt.show()