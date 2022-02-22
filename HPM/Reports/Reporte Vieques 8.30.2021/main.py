import pandas as pd

df_visits = pd.read_excel("13.07 - Visit Counts.xlsx")
df_edades = pd.read_excel("edades.xlsx")
df_edades.rename(columns={"Patient Acct No": "Patient Account Number"}, inplace=True)

df_merged = pd.merge(df_visits, df_edades, on="Patient Account Number")
df_merged = df_merged[df_merged["Patient Age"] <= 15]

df_merged.sort_values("Patient Age", inplace=True)
df_merged = df_merged[
    ["Patient Name", "Patient Account Number", "Visit Count", "Patient Age"]
]
df_merged.to_excel("Reporte 8.30.2021 - Vieques.xlsx", index=False)

print(df_merged.info())
