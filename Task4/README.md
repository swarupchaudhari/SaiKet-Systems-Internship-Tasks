# 📊 Task 4: Churn Rates by Gender

## 📌 Objective

The objective of this task is to compare churned and non-churned customers across different genders. This analysis helps determine whether customer churn behavior varies between male and female customers.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

Important columns used:

* gender
* Churn
* customerID

---

## 🛠️ Tools Used

* Python
* Pandas
* Matplotlib

---

## 📋 Steps Performed

### 1. Load Dataset

The Telco Customer Churn dataset was loaded using Pandas.

### 2. Create Pivot Table

A Pivot Table was created using:

* Rows: Gender
* Columns: Churn Status
* Values: Customer Count

This provides churned and non-churned customer counts for each gender.

### 3. Create Clustered Bar Chart

The Pivot Table data was visualized using a Clustered Bar Chart.

Chart Components:

* X-Axis: Gender
* Y-Axis: Customer Count
* Bars:

  * Churned Customers
  * Non-Churned Customers

### 4. Apply Formatting

* Added chart title
* Added axis labels
* Added legend
* Used distinct colors for churn categories

---

## 📈 Key Insights

### Insight 1

Both male and female customers show similar churn patterns.

### Insight 2

The number of non-churned customers is higher than churned customers for both genders.

### Insight 3

Gender alone may not be a strong predictor of customer churn.

### Insight 4

Additional factors such as tenure, contract type, and monthly charges may have greater influence on churn behavior.

---

## 📊 Business Value

This analysis helps organizations:

* Understand customer retention by gender
* Identify demographic trends
* Support customer segmentation strategies
* Improve targeted retention campaigns

---

## 🚀 Skills Demonstrated

* Pivot Tables
* Clustered Bar Charts
* Data Aggregation
* Customer Churn Analysis
* Data Visualization
* Python Programming

---

## ✅ Conclusion

The analysis compared churn behavior across genders using a Pivot Table and Clustered Bar Chart. Results indicate that churn patterns are relatively similar for male and female customers, suggesting that other customer attributes may play a larger role in predicting churn.
