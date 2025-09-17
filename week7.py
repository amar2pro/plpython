# Assignment: Pandas & Matplotlib Data Analysis
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Task 1: Load and Explore the Dataset
# Load Iris dataset from sklearn
iris_data = load_iris(as_frame=True)
df = iris_data.frame

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Check structure of dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# (No missing values in Iris, but let’s show how to handle them)
# Example: df.fillna(method="ffill", inplace=True)


# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping: average petal length per species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Interesting finding
print("\nObservation: Species 2 (Virginica) has the longest average petal length.")


# Task 3: Data Visualization
# 1. Line Chart (simulate time trend using index)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart of Sepal & Petal Lengths Over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(6,4))
grouped.plot(kind="bar", color=["skyblue", "lightgreen", "salmon"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=20, color="purple", alpha=0.7)
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(6,5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

# Findings / Observations


print("""
Findings:
1. The dataset has no missing values.
2. Virginica species tends to have the longest petals.
3. Sepal length and petal length show a strong positive relationship.
4. The histogram shows most sepal widths are clustered between 2.5 - 3.5 cm.
""")
