import pandas as pd

df = pd.read_excel("Patient Ages 01.01.2013-01.04.2022.xlsx")

filter = df["Patient Age Group"].isin(["Under 18 Yrs"])

filter = df["Appointment Facility Name"].isin(["Healthpromed Vieques"])

filter = df["Patient Status"].isin(["Active"])

print(df.head())
