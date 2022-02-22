import pandas as pd

df = pd.read_excel("Decomissions.xlsx")

df["HPM Tag"] = df["HPM Tag"].astype(str)
df.sort_values("Equipment Type", inplace=True)
# df.to_excel("Decomissions_Sorted.xlsx", index=False)
print(df.info())