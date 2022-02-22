import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pdfer as pdf


df_p8 = pd.read_excel("P8. PRAPARE Frequency of Diagnosis.xlsx")

df_p5 = pd.read_excel("P5. PRAPARE Social Determinants Analysis.xlsx")

list_p8 = df_p8["PatientAccountNumber"].values.tolist()

df_p5 = df_p5[df_p5["PatientAccountNumber"].isin(list_p8)]

category_list = df_p5["Category"].unique().tolist()

save_path = "C:/PNG/"

for category in category_list:
    df = df_p5[df_p5["Category"] == category]["Response"].value_counts()
    df = df.reset_index()
    df.rename(columns={"index": "Category"}, inplace=True)
    sns.set(rc={"figure.figsize": (7, 9.5)})
    sns.barplot(x="Category", y="Response", data=df).set_title(category)
    plt.tight_layout()
    file = f"./imagenes/{category}.png"
    plt.savefig(file)
