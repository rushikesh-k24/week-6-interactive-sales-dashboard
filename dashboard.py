import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

print("Week 6: Interactive Sales Dashboard\n")


df = pd.read_csv("sales_data.csv")


df["Date"] = pd.to_datetime(df["Date"])
df["Total_Sales"] = df["Quantity"] * df["Price"]

# BOX PLOT

plt.figure()
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")

plt.show(block=False)
plt.pause(3)
plt.close()

# BAR CHART 

product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure()
sns.barplot(x=product_sales.index, y=product_sales.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show(block=False)
plt.pause(3)
plt.close()

# LINE CHART

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure()
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.show(block=False)
plt.pause(3)
plt.close()

# HEATMAP

plt.figure()
corr = df[["Quantity", "Price", "Total_Sales"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show(block=False)
plt.pause(3)
plt.close()

# SUBPLOTS DASHBOARD

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Plot 1
sns.boxplot(x="Product", y="Price", data=df, ax=axes[0, 0])
axes[0, 0].set_title("Price Distribution")

# Plot 2
sns.barplot(x=product_sales.index, y=product_sales.values, ax=axes[0, 1])
axes[0, 1].set_title("Sales by Product")

# Plot 3
axes[1, 0].plot(daily_sales.index, daily_sales.values)
axes[1, 0].set_title("Sales Trend")

# Plot 4
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[1, 1])
axes[1, 1].set_title("Correlation")

plt.tight_layout()

plt.show(block=False)
plt.pause(5)
plt.close()

print("Dashboard execution completed successfully")