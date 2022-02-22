import pandas as pd

df = pd.read_excel("New Report.xlsx")

# df[df["Primary Insurance Name"].str.contains("MMM ADVANTAGE") == True]

filter = df["Primary Insurance Name"].isin(
    ["MMM ADVANTAGE", "MCS", "TRIPLE S ADVANTAGE"]
)

df[filter].sort_values(by=["Primary Insurance Name"], ascending=True)

final = df.loc[
    filter,
    [
        "Patient Name",
        "Patient Cell Phone",
        "Patient Home Phone",
        "Patient E-mail",
        "Primary Insurance Name",
    ],
]

final.sort_values(by=["Primary Insurance Name"], ascending=True).to_excel(
    "txt_b.xlsx", index=False
)

print(df[filter].head())
