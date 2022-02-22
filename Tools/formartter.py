import pandas as pd

df = pd.read_excel("unformatted_data.xlsx")

df["data"] = "HPM-" + df["data"].astype(str).str.zfill(5)

# df["data"] = df["data"].astype(str)
# for _, num in df.iterrows():
#     while len(num.values[0]) < 5:
#         num.values[0] = "0" + num.values[0]
#     num.values[0] = "HPM-" + num.values[0]

print(df)
