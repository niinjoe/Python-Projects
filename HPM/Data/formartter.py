import pandas as pd

df = pd.read_excel("Decomissions_copy.xlsx")
# df["HPM Tag"] = df["HPM Tag"].astype(int)
# df["HPM Tag"] = "HPM-" + df["HPM Tag"].astype(str).str[:-2].str.zfill(5)

df["HPM Tag"] = df["HPM Tag"].astype(str).str[:-2]

for _, num1 in df.iterrows():
    num = num1[0]
    if num != "n":
        while len(num) < 5:
            num = "0" + num
        num1[0] = "HPM-" + num
    else:
        num1[0] = ""

df.to_excel("Decomissions_Copy_Fixed.xlsx", index=False)
