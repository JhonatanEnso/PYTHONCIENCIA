import matplotlib.pyplot as plt

x = ['Betis', 'Atletico Madrid', 'Real Madrid', 'Barcelona']
y = [5, 10, 15, 20]

# Creamos el gráfico de barras

plt.plot(x, y)

plt.title('Goles de los equipos')
plt.xlabel('Equipos')
plt.ylabel('Goles')

plt.savefig('/Users/tardes/Documents/CIENCIADEDATOS/PYTHONCIENCIA/images/grafico22lineal.png')
plt.show()