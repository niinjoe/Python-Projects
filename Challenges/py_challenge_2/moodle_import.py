import pandas as pd

df = pd.read_csv("export.csv", skiprows=1)

# df2 = pd.read_csv("prueba_usuarios.csv")

# df["username"] = df["mail"]

# # df["username"] = df["username"].str.replace("@healthpromed.org", "")

# df["username"] = df["username"].str[:-17]

# df2.rename(
#     columns={
#         "E-Mail Address": "mail",
#         "First Name": "firstname",
#         "Last Name": "lastname",
#     },
#     inplace=True,
# )

# df = df[["mail", "username"]]

# df_merge = pd.merge(df, df2, on="mail")

# df_merge.rename(columns={"mail": "email"}, inplace=True)

# df_merge = df_merge[["username", "firstname", "lastname", "email"]]

# df_merge.to_csv("exported_users.csv", index=False)

# TODO Find a way to eliminate initials, then split first name from last names extracted from "exported_users".

df["nombre"] = df["name"].str.split(" ", 1).str[0]
df["apellidos_plus"] = df["name"].str.split(" ", 1).str[1]

# df.loc[df["apellidos_plus"].str.contains("."), "Middle"] = (
#     df["apellidos_plus"].str.split(" ", 1).str[0]
# )
print(len(df[df[]]))
