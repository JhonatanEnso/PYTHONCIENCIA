import pandas as pd

print("lecturas de csv")

df = pd.read_csv('data/datos.csv', delimiter=';')
print(df)
df_sorted = df.sort_values(by='edad')
print(df_sorted)

media_edad =df['edad'].mean()
print(media_edad)