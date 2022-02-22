import pandas as pd

df = pd.read_excel("source.xlsx")

df["Number"] = df["NU"].str.split(".").str[0].str.strip()

df["Combination"] = df["NU"].str.split(".").str[1].str.strip()

df = df[["Number", "Combination"]]

df.to_excel("split.xlsx", index=False)
