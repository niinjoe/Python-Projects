import pandas as pd

df_ac = pd.read_excel("13.07 - Visit Counts (1).xlsx")
df_er = pd.read_excel("4.16 - Telephone_Web Encounters.xlsx")

df_ac["AcctNo"] = df_ac["Patient Acct No"].str.split(":").str[0].str.strip()


print(df_ac.head())

df_ac.to_excel("test.xlsx", index=False)
