import pandas as pd

df = pd.read_excel("Reporte Vacunados por dia.xlsx", skiprows=2)

visit = ["Check Out", "Check-in"]

### if True, removes everything but what is specified. If False, remove what is specified.
df = df[df["Visit Status"].isin(visit) == True]

dups = df.pivot_table(columns=["Appointment Date"], aggfunc='size')

df2 = dups.reset_index()
df2.columns = df2.columns.str.replace("0", "Conteo Total")
df2.rename(columns={df2.columns[1]: "Conteo Total"})

# df2.to_excel("Reporte Vacunados por dia_SUM.xlsx", index=False)

print(df2.head())
