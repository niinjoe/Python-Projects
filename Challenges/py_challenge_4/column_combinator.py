import pandas as pd

df = pd.read_csv("marca_modelo.csv")

df["Marca y Modelo"] = df["1"] + ' - ' + df["2"]

print(df.head())

df.to_csv("combinados.csv", index=False)