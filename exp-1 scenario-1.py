print("Kamalesh.M\t\tMachine Learning Ex-1\t\t24BAD053")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data_path = r"C:\Users\91638\Hospital_Patient_Records.csv"
data = pd.read_csv(data_path)

# -------------------------------
# Data Inspection
# -------------------------------
print("\n\t\tData Inspection:\n")

print("First 5 rows:\n")
print(data.head())

print("\nLast 5 rows:\n")
print(data.tail())

print("\nDataset Info:\n")
data.info()   # No need to print again

print("\nStatistical Summary:\n")
print(data.describe())

# -------------------------------
# Missing Values
# -------------------------------
print("\nMissing Values in Each Column:\n")
print(data.isnull().sum())

# -------------------------------
# Visualizations
# -------------------------------

# Histogram - Glucose
if 'Glucose' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Glucose'], kde=True, color='skyblue')
    plt.title("Glucose Level Distribution")
    plt.xlabel("Glucose")
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot - Glucose
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['Glucose'], color='skyblue')
    plt.title("Glucose Level Boxplot")
    plt.xlabel("Glucose")
    plt.show()

# Histogram - Age
if 'Age' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'], kde=True, color='lightgreen')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot - Age
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=data['Age'], color='lightgreen')
    plt.title("Age Boxplot")
    plt.xlabel("Age")
    plt.show()

# -------------------------------
# Correlation Analysis
# -------------------------------

# Select only numeric columns
numeric_data = data.select_dtypes(include=['number'])
correlation = numeric_data.corr()

print("\nCorrelation Matrix:\n")
print(correlation)

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix Heatmap")
plt.show()
