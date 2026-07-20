# 📊 Task 5: Heatmap for Monthly Charges and Tenure Interaction

## 📌 Objective

The objective of this task is to analyze the relationship between **Monthly Charges**, **Tenure**, and **Customer Churn** using a Heatmap. This visualization helps identify patterns in customer behavior and understand which customer groups are more likely to churn.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

### Columns Used

* tenure
* MonthlyCharges
* Churn

---

## 🎯 Problem Statement

Customer churn is influenced by multiple factors. Two important factors are:

* How long a customer has stayed with the company (Tenure)
* How much a customer pays monthly (Monthly Charges)

A Heatmap helps visualize how these factors interact and how they relate to churn behavior.

---

## 🛠️ Tools Used

* Microsoft Excel
* Conditional Formatting
* Pivot Tables
* Data Analysis Techniques

---

## 📋 Steps Performed

### Step 1: Data Cleaning

Before creating the heatmap:

* Checked for missing values
* Verified Monthly Charges values
* Verified Tenure values
* Removed invalid records if necessary

### Step 2: Create Tenure Groups

Customers were grouped into tenure ranges:

* 0–12 Months
* 13–24 Months
* 25–36 Months
* 37–48 Months
* 49–60 Months
* 61–72 Months

### Step 3: Create Monthly Charge Groups

Monthly charges were grouped into intervals:

* $0–20
* $20–40
* $40–60
* $60–80
* $80–100
* $100–120

### Step 4: Create Pivot Table

Pivot Table Configuration:

Rows:

* Tenure Group

Columns:

* Monthly Charge Group

Values:

* Count of Customers

Filter:

* Churn Status

### Step 5: Apply Heatmap

Using Excel Conditional Formatting:

Home → Conditional Formatting → Color Scales

A color gradient was applied where:

* Dark Color = Higher Customer Count
* Light Color = Lower Customer Count

---

## 📈 Heatmap Interpretation

The heatmap highlights areas where customer concentrations are highest.

### Example Observations

#### High Customer Concentration

Customers with:

* Long Tenure
* Medium Monthly Charges

typically represent loyal customers.

#### High Churn Risk Segment

Customers with:

* Short Tenure
* High Monthly Charges

often show a higher tendency to churn.

#### Stable Customer Segment

Customers with:

* Long Tenure
* Consistent Monthly Charges

are generally less likely to leave.

---

## 🔍 Key Insights

### Insight 1

Monthly Charges and Tenure together influence customer retention.

### Insight 2

Customers paying higher charges during early months are more likely to churn.

### Insight 3

Long-term customers demonstrate stronger loyalty.

### Insight 4

Heatmaps make it easier to identify customer segments requiring retention strategies.

---

## 📊 Business Value

This analysis helps businesses:

* Identify high-risk customer groups
* Improve customer retention
* Optimize pricing strategies
* Design targeted marketing campaigns
* Reduce customer churn

---

## 🚀 Skills Demonstrated

### Excel Skills

✓ Pivot Tables

✓ Conditional Formatting

✓ Heatmap Creation

### Data Analysis Skills

✓ Data Cleaning

✓ Customer Segmentation

✓ Churn Analysis

✓ Data Interpretation

✓ Exploratory Data Analysis (EDA)

---

## ✅ Conclusion

The Heatmap successfully visualized the interaction between Monthly Charges and Tenure. The analysis revealed important customer behavior patterns and highlighted groups with higher churn risk. These insights can support data-driven business decisions and customer retention strategies.
