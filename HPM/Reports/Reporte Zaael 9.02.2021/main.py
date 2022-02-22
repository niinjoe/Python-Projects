import pandas as pd

# df_age = pd.read_excel("edades_y_numeros.xlsx")
# df_cpt = pd.read_excel("cpt_codes.xlsx")

# df_cpt = df_cpt[df_cpt["CPT Code"] == "82274"]

# df_merged = pd.merge(df_age, df_cpt, on = "Patient Acct No")

# df_merged.to_excel("Reporte Solicitado.xlsx", index=False)

df_new = pd.read_excel("Reporte Solicitado.xlsx")
df_og = pd.read_excel(
    "Table 6B.xlsx", skiprows=1, sheet_name="MS SQL Detail_2", skipfooter=2
)

df_new.rename(columns={"Patient Acct No": "Account No"}, inplace=True)

df_merged = pd.merge(df_new, df_og, on="Account No", how="right")
df_merged = df_merged[
    [
        "Account No",
        "CPT Code",
        "Patient Name",
        "Patient Age",
        "Date of Birth",
        "Demographic PCP",
        "Demographic Rendering Provider",
        "Patient Home Phone",
        "Patient Cell Phone",
        "Numerator",
    ]
]
df_merged["Date of Birth"] = df_merged["Date of Birth"].dt.date

df_merged = df_merged.sort_values(
    by=["Numerator", "Patient Name"], ascending=[False, True]
)
df_merged.to_excel("Reporte Final1.xlsx", index=False)
