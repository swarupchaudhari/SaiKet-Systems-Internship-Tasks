```python
# Task 5: Heatmap for Monthly Charges and Tenure Interaction

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Telco_Customer_Churn_Dataset.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Convert TotalCharges if needed
if 'TotalCharges' in df.columns:
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove missing values
df = df.dropna(subset=['tenure', 'MonthlyCharges', 'Churn'])

# -----------------------------
# Create Tenure Groups
# -----------------------------

tenure_bins = [0, 12, 24, 36, 48, 60, 72]
tenure_labels = [
    '0-12',
    '13-24',
    '25-36',
    '37-48',
    '49-60',
    '61-72'
]

df['Tenure_Group'] = pd.cut(
    df['tenure'],
    bins=tenure_bins,
    labels=tenure_labels,
    include_lowest=True
)

# -----------------------------
# Create Monthly Charge Groups
# -----------------------------

charge_bins = [0, 20, 40, 60, 80, 100, 120]
charge_labels = [
    '0-20',
    '20-40',
    '40-60',
    '60-80',
    '80-100',
    '100-120'
]

df['Charge_Group'] = pd.cut(
    df['MonthlyCharges'],
    bins=charge_bins,
    labels=charge_labels,
    include_lowest=True
)

# -----------------------------
# Create Pivot Table
# -----------------------------

pivot_table = pd.pivot_table(
    df,
    values='customerID',
    index='Tenure_Group',
    columns='Charge_Group',
    aggfunc='count',
    fill_value=0
)

print("Pivot Table:")
print(pivot_table)

# -----------------------------
# Create Heatmap
# -----------------------------

plt.figure(figsize=(10, 6))

plt.imshow(
    pivot_table,
    aspect='auto'
)

plt.colorbar(label='Customer Count')

plt.xticks(
    range(len(pivot_table.columns)),
    pivot_table.columns,
    rotation=45
)

plt.yticks(
    range(len(pivot_table.index)),
    pivot_table.index
)

plt.title("Heatmap of Monthly Charges and Tenure Interaction")
plt.xlabel("Monthly Charges Group")
plt.ylabel("Tenure Group")

# Add values inside heatmap
for i in range(len(pivot_table.index)):
    for j in range(len(pivot_table.columns)):
        plt.text(
            j,
            i,
            pivot_table.iloc[i, j],
            ha='center',
            va='center'
        )

plt.tight_layout()
plt.show()

# -----------------------------
# Churn Analysis
# -----------------------------

churn_summary = pd.pivot_table(
    df,
    values='customerID',
    index='Tenure_Group',
    columns='Churn',
    aggfunc='count',
    fill_value=0
)

print("\nChurn Summary:")
print(churn_summary)
```
