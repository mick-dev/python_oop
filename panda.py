import pandas
df = pandas.read_csv("Pandas - Q1 Sales.csv")
# print(df.head())
# print(df.describe())
# print(df.columns.values)

# selecting columns
# columns = ["Total", "Quantity", "Country"]
# print(df[columns])
# print(df.loc[columns])

# selecting rows
# print(df.iloc[0:3, :])

row_index = [0, 1, 4, 5]
print(df.loc[row_index])
print(df.loc[])