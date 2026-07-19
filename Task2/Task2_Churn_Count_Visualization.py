
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Count churn values
churn_counts = df["Churn"].value_counts()

print("Churn Counts:")
print(churn_counts)

# Plot Column Chart
plt.figure(figsize=(6,4))
churn_counts.plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

# Add labels
for i, v in enumerate(churn_counts):
    plt.text(i, v, str(v), ha="center")

plt.tight_layout()
plt.show()

# Insights
total = churn_counts.sum()
churn_rate = (churn_counts.get("Yes", 0) / total) * 100

print(f"Total Customers: {total}")
print(f"Churn Rate: {churn_rate:.2f}%")
