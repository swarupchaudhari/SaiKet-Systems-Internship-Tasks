import pandas as pd

# Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

print("="*50)
print("DATASET OVERVIEW")
print("="*50)

# Structure
print("\nDataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# Sort by Tenure
print("\n" + "="*50)
print("CUSTOMERS WITH SHORTEST TENURE")
print("="*50)
print(df.sort_values("tenure", ascending=True).head(10))

print("\n" + "="*50)
print("CUSTOMERS WITH LONGEST TENURE")
print("="*50)
print(df.sort_values("tenure", ascending=False).head(10))

# Filter churned customers
churned = df[df["Churn"] == "Yes"]

print("\n" + "="*50)
print("CHURNED CUSTOMERS")
print("="*50)
print(churned.head())

print("\nTotal Customers:", len(df))
print("Churned Customers:", len(churned))
print("Non-Churned Customers:", len(df[df["Churn"] == "No"]))

# Save filtered data
churned.to_csv("Churned_Customers.csv", index=False)

print("\nFiltered churned customer data saved as: Churned_Customers.csv")

print("\nTask 1 Completed Successfully!")
