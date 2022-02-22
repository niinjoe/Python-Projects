import pandas as pd
import time
from styleframe import StyleFrame

tic = time.perf_counter()
print("%.2f" % tic)
df_appt = pd.read_excel("appt_date.xlsx")
df_icd = pd.read_excel("icd_codes.xlsx")

df_merge = pd.merge(df_icd, df_appt, on="Patient Acct No")

df_merge = df_merge[df_merge["ICD Code"] == "R76.11"]

df_merge.drop_duplicates(subset="Patient Acct No", keep="first", inplace=True)

print(df_merge.info())

columns = [
    "Appointment Date",
    "Patient Acct No",
    "Patient Age",
    "Patient Gender",
    "Primary Insurance Name",
    "ICD Code",
]

excel_writer = StyleFrame.ExcelWriter("report_end.xlsx")
sf = StyleFrame(df_merge)
sf.to_excel(
    excel_writer=excel_writer,
    best_fit=columns,
    columns_and_rows_to_freeze="B2",
    row_to_add_filters=0,
)
excel_writer.save()

toc = time.perf_counter()
print("%.2f" % toc)
