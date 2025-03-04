import pandas as pd

print("hola mundo")

datos = {'nombres': ['Juan', 'Ana', 'Pedro', 'Marta'],
         'edades': [25, 30, 45, 33],
         'ciudades': ['Bogotá', 'Medellín', 'Cali', 'Bogotá']}









print("-----dataframe filtrado------")
df_filtrado = df[df['edades'] > 30]
print(df_filtrado)

print("-----dataframe filtrado por ciudad------")