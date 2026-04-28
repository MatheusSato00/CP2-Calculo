import numpy as np
import matplotlib.pyplot as plt

#Questão 5 - Redução de erros após ajuste de um sistema

#intervalo de dias
x2 = np.linspace(0, 10, 300)

#função R(s)
y2 = 120*(0.72**x2)

#ponto específico
x2_ponto = 9
y2_ponto = 120*(0.72**x2_ponto)

#grafico
plt.figure(figsize=(10, 4.5))
plt.plot(x2, y2, label="R(s) = Erros")
plt.scatter([x2_ponto], [y2_ponto], color='red', label="s = 9")
plt.xlabel("Dias após atualização")
plt.ylabel("Número de erros")
plt.title("Questão 5 - Redução de Erros - Matheus Sato - Rm569392")
plt.grid(True)
plt.legend()
plt.show()