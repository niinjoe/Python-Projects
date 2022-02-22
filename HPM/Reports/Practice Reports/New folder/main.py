import pandas as pd
from styleframe import StyleFrame


df = pd.read_excel("13.07 - Visit Counts (1).xlsx")

df.rename(columns={"Patient Acct No": "AcctNo"}, inplace=True)

df["PtAccNo"] = df["AcctNo"].str.split(":").str[0].str.strip()

df["PtName"] = df["AcctNo"].str.split(":").str[1].str.strip()

df = df[["PtAccNo", "PtName", "Patient Gender"]]

columns = ["PtAccNo", "PtName", "Patient Gender"]

excel_writer = StyleFrame.ExcelWriter("Name & Gender.xlsx")
sf = StyleFrame(df)
sf.to_excel(
    excel_writer=excel_writer,
    best_fit=columns,
    columns_and_rows_to_freeze="B2",
    row_to_add_filters=0,
)
excel_writer.save()
