import pandas as pd

df_cpt = pd.read_excel("n_cpt_codes.xlsx")
df_icd = pd.read_excel(
    "n_icd_codes.xlsx", skiprows=6, sheet_name="ICD Detail_2", skipfooter=4
)

df_merge = pd.merge(df_cpt, df_icd, on="Patient Acct No")

df_merge = df_merge[
    [
        "Patient Acct No",
        "CPT Code",
        "ICD Code",
        "Patient Name",
        "Primary Insurance Name",
    ]
]

df_merge.drop_duplicates(subset="Patient Acct No", keep="first", inplace=True)

df_merge = df_merge[df_merge["CPT Code"] == "92250"]

print(df_merge.head())

from styleframe import StyleFrame

columns = [
    "Patient Acct No",
    "CPT Code",
    "ICD Code",
    "Patient Name",
    "Primary Insurance Name",
]

excel_writer = StyleFrame.ExcelWriter("Report Draft_3.xlsx")
sf = StyleFrame(df_merge)
sf.to_excel(
    excel_writer=excel_writer,
    best_fit=columns,
    columns_and_rows_to_freeze="B2",
    row_to_add_filters=0,
)
excel_writer.save()
