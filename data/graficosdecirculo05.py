#terminar de corregir el codigo

import matplotlib.pyplot as plt



temperaturas = []
dias_semana = []
for i in range(7):
    temp = float(input(f'Introduce la temperatura del dia {i+1}: '))
    if temp != float:
        print("introduce denuevo el valor numerico" + temp)

    else:
        temperaturas.append(temp)
        break
        
    
    dias_semana.append(f'Dia {i+1}')
 

plt.pie(precios, labels=productos)
plt.title('Grafico de Tarta')
plt.savefig('images/grafico25tarta05.png')
plt.show()
