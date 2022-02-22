from styleframe import StyleFrame

columns = ["A", "B", "C"]

excel_writer = StyleFrame.ExcelWriter("desired name.xlsx")
sf = StyleFrame("dataframe to use")
sf.to_excel(
    excel_writer=excel_writer,
    best_fit=columns,
    columns_and_rows_to_freeze="B2",
    row_to_add_filters=0,
)
excel_writer.save()

# source documentation: https://styleframe.readthedocs.io/en/latest/index.html
