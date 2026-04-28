import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 12, 300)
A = 250*(1.15**x)
 
x_ponto = 4
A_ponto = 250*(1.15**x_ponto)
 
plt.figure(figsize=(10,4.5))
plt.plot(x, A)
plt.scatter([x_ponto], [A_ponto], color='red')
plt.xlabel("Meses")
plt.ylabel("Acessos (milhares)")
plt.title("Questão 4 - Crescimento de acessos - Matheus Sato - Rm569392")
plt.grid(True)
plt.show()