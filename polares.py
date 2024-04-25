import numpy as np
import matplotlib.pyplot as plt

# Definir el ángulo theta
theta = np.linspace(0, np.pi/2, 100)

# Definir los radios r para cada valor de theta
r_min = np.zeros_like(theta)
r_max = 1 + np.sin(theta)

# Crear un gráfico polar
ax = plt.subplot(111, polar=True)

# Dibujar la región de integración
for i in range(len(theta)):
    ax.fill_between([0, theta[i]], r_min[i], r_max[i], color='skyblue', alpha=0.5)

# Configurar el gráfico
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rticks(np.arange(0, 2, 0.5))
ax.set_title('Región de integración en coordenadas polares')

# Mostrar el gráfico
plt.show()
