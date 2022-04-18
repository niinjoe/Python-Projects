import pandas as pd

df = pd.read_excel("Reporte PCF.xlsx")

df.drop_duplicates(subset="Patient Name", keep="first", inplace=True)

df.to_excel("Reporte_dropduplicates.xlsx", index=False)