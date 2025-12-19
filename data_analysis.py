"""
MinervaBI – Business Intelligence Data Analysis
Author: MinervaBI Startup Project
Description:
This script analyzes SME business data to extract actionable insights
related to conversion, retention, efficiency, and trends.
"""

import pandas as pd

# ===============================
# 4.1 Data Sources & Collection
# ===============================
# Simulated integrated dataset from CRM, Analytics, and Surveys
# (In real deployment, data comes from APIs and databases)

file_path = r'C:\Users\For Students\Downloads\sme_business_data.csv'
data = pd.read_csv(file_path)

# Convert date column
data["date"] = pd.to_datetime(data["date"])

# ===============================
# Basic Data Overview
# ===============================
print("=== Data Overview ===")
print(data.head())
print("\nData Summary:")
print(data.describe())

# ===============================
# Key Performance Indicators (KPIs)
# ===============================

data["profit"] = data["revenue"] - data["cost"]

total_revenue = data["revenue"].sum()
total_profit = data["profit"].sum()
average_customers = data["customers"].mean()

print("\n=== Key Business Metrics ===")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Customers: {average_customers:.0f}")

# ===============================
# 4.2 Findings & Insights
# ===============================

# A/B Testing: Dashboard Simplicity vs Complex Design
ab_test_results = data.groupby("dashboard_version").agg({
    "conversion_rate": "mean",
    "retention_rate": "mean"
})

print("\n=== A/B Testing Results ===")
print(ab_test_results)

conversion_lift = (
    ab_test_results.loc["simplified", "conversion_rate"]
    - ab_test_results.loc["complex", "conversion_rate"]
) * 100

print(f"\nConversion Lift from Simplified Dashboards: {conversion_lift:.2f}%")

# Time savings from automation
average_time_saved = data["hours_saved_per_week"].mean()
print(f"Average Time Saved per SME per Week: {average_time_saved:.1f} hours")

# ===============================
# 4.3 Trend and Risk Analysis
# ===============================

# Monthly trends
monthly_trends = data.resample("M", on="date").agg({
    "revenue": "sum",
    "customers": "sum",
    "conversion_rate": "mean",
    "retention_rate": "mean"
})

print("\n=== Monthly Trends ===")
print(monthly_trends)

# Risk indicators
churn_risk = data[data["retention_rate"] < 0.7]
high_risk_regions = churn_risk["region"].value_counts()

print("\n=== Churn Risk Regions ===")
print(high_risk_regions)

# ===============================
# 5. Results and Discussion
# ===============================

decision_efficiency_gain = (
    data["hours_saved_per_week"].mean() / 40
) * 100

print("\n=== Decision-Making Efficiency ===")
print(f"Estimated Efficiency Improvement: {decision_efficiency_gain:.2f}%")

# ===============================
# Export BI Reports
# ===============================

monthly_trends.to_csv("monthly_trend_report.csv")
ab_test_results.to_csv("ab_testing_report.csv")
high_risk_regions.to_csv("risk_analysis_report.csv")

print("\nBI reports generated successfully.")
