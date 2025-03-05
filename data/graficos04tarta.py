import matplotlib.pyplot as plt

etiquetas = ['Betis', 'Atletico Madrid', 'Real Madrid', 'Barcelona']
valores = [5, 10, 15, 20]

plt.pie(valores, labels=etiquetas, autopct= '%1.1f%%')
plt.title('Grafico de Tarta')
plt.savefig('images/grafico24tarta.png')
plt.show()