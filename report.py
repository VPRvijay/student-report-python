# Student Marks Report Generator
# RISE Internship - Python Programming
# Author: Vijay

import pandas as pd
import matplotlib.pyplot as plt
import os

# ── 1. LOAD DATA ──────────────────────────────────────────
df = pd.read_csv("students.csv")
print("✅ Data loaded successfully!")
print(df)

# ── 2. CLEAN DATA ─────────────────────────────────────────
df = df.dropna()  # Remove empty rows
print("\n✅ Data cleaned!")

# ── 3. CALCULATE METRICS ──────────────────────────────────
subjects = ["Math", "Science", "English", "Tamil", "Computer"]

df["Total"]   = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)
df["Grade"]   = df["Average"].apply(lambda x:
    "A+" if x >= 90 else
    "A"  if x >= 80 else
    "B"  if x >= 70 else
    "C"  if x >= 60 else "F")

print("\n✅ Metrics calculated!")
print(df[["Name","Total","Average","Grade"]])

# ── 4. SUMMARY ────────────────────────────────────────────
print("\n📊 Class Summary:")
print(f"  Highest Average : {df['Average'].max()} - {df.loc[df['Average'].idxmax(), 'Name']}")
print(f"  Lowest Average  : {df['Average'].min()} - {df.loc[df['Average'].idxmin(), 'Name']}")
print(f"  Class Average   : {df['Average'].mean().round(2)}")

# ── 5. SAVE REPORT ────────────────────────────────────────
df.to_csv("report_output.csv", index=False)
print("\n✅ Report saved as report_output.csv")

# ── 6. CHART ──────────────────────────────────────────────
plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Average"], color="steelblue")
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart.png")
plt.show()
print("✅ Chart saved as chart.png")
