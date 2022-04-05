import pandas as pd

df = pd.read_csv("export.csv", skiprows=1)

df2 = pd.read_csv("prueba_usuarios.csv")

df["username"] = df["mail"]

# df["username"] = df["username"].str.replace("@healthpromed.org", "")

df["username"] = df["username"].str[:-17]

df2.rename(
    columns={
        "E-Mail Address": "mail",
        "First Name": "firstname",
        "Last Name": "lastname",
    },
    inplace=True,
)

df = df[["mail", "username"]]

df_merge = pd.merge(df, df2, on="mail")

df_merge.rename(columns={"mail": "email"}, inplace=True)

df_merge = df_merge[["username", "firstname", "lastname", "email"]]

df_merge.to_csv("exported_users.csv", index=False)
