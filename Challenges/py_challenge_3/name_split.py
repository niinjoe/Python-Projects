# TODO Find a way to eliminate initials, then split first name from last names extracted from "exported_users".

import pandas as pd

df = pd.read_csv("export.csv", skiprows=1)

df["nombre"] = df["name"].str.split(" ", 1).str[0]

df["apellidos"] = df["name"].str.split(".").str[:]

# df.loc[df["apellidos_plus"].str.contains("."), "Middle"] = (
#     df["apellidos_plus"].str.split(" ", 1).str[0]
# )

print(df.head(15))