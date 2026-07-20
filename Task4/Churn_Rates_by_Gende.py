```python
# Task 4: Churn Rates by Gender

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# Create Pivot Table
pivot_table = pd.pivot_table(
    df,
    index="gender",
    columns="Churn",
    values="customerID",
    aggfunc="count",
    fill_value=0
)

print("Pivot Table:")
print(pivot_table)

# Create Clustered Bar Chart
pivot_table.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Churn Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Customer Count")
plt.legend(title="Churn Status")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
```
