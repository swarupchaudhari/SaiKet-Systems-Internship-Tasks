```python
# Task 3: Monthly Charges Distribution

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Display Basic Information
print("Dataset Shape:", df.shape)
print("\nMonthly Charges Summary:")
print(df["MonthlyCharges"].describe())

# Create Histogram
plt.figure(figsize=(10, 6))

plt.hist(
    df["MonthlyCharges"],
    bins=10,           # Interval size
    edgecolor="black"
)

# Chart Formatting
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges ($)")
plt.ylabel("Number of Customers")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
```
