import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../Data/Global_Superstore2.csv", encoding="latin1")

print("Dataset preview:")
print(df.head())


total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)


top_countries = df.groupby("Country")["Sales"].sum().sort_values(ascending=False)

print("\nTop Countries:")
print(top_countries.head(10))


profit_country = df.groupby("Country")["Profit"].sum().sort_values(ascending=False)

print("\nProfit by Country:")
print(profit_country.head(10))


top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print("\nTop Products:")
print(top_products.head(10))


df["Order Date"] = pd.to_datetime(df["Order Date"])
sales_year = df.groupby(df["Order Date"].dt.year)["Sales"].sum()

plt.figure()
sales_year.plot(kind="line", marker="o")
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.savefig("../images/sales_by_year.png")


sales_category = df.groupby("Category")["Sales"].sum()

plt.figure()
sales_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("../images/sales_by_category.png")



plt.figure()
top_countries.head(10).plot(kind="bar")
plt.title("Top Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.savefig("../images/top_countries.png")


plt.figure()
top_products.head(10).plot(kind="bar")
plt.title("Top Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("../images/top_products.png")
plt.show()
