import pandas as pd

df_list = pd.read_excel(
    "Lista_Equipos_Decomiso_2021.xlsx", skiprows=13, sheet_name="FORM TRANSF 23"
)
df_source = pd.read_excel("Decomissions_Copy_Fixed.xlsx")
