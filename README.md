# Data Analytics with Pandas and NumPy

## Overview

This repository contains my practice and projects in Data Analytics using Python, Pandas, and NumPy.

The focus is on understanding how to work with datasets, clean and transform data, perform exploratory data analysis, calculate statistical values, and extract meaningful insights from raw data.

## Objectives

* Learn data analytics using Python.
* Understand NumPy for numerical computations.
* Learn Pandas for data manipulation and analysis.
* Practice data cleaning and preprocessing.
* Analyze real-world datasets.
* Perform exploratory data analysis.
* Handle missing and duplicate data.
* Perform statistical analysis.
* Create meaningful insights from datasets.
* Build a strong foundation in Data Analytics.

## Technologies Used

* Python
* NumPy
* Pandas
* Jupyter Notebook
* VS Code
* Kaggle Datasets

## NumPy Concepts

The following NumPy concepts are practiced:

* Creating NumPy arrays
* Array indexing
* Array slicing
* Array reshaping
* Array dimensions
* Array operations
* Mathematical operations
* Statistical functions
* Mean
* Median
* Standard deviation
* Minimum and maximum values
* Random number generation
* Broadcasting
* Matrix operations

## Pandas Concepts

The following Pandas concepts are practiced:

* Series
* DataFrame
* Reading CSV files
* Reading Excel files
* DataFrame inspection
* Selecting columns
* Selecting rows
* Filtering data
* Sorting data
* Adding columns
* Removing columns
* Renaming columns
* Handling missing values
* Removing duplicates
* GroupBy operations
* Aggregation
* Merging datasets
* Joining datasets
* Concatenating datasets
* Pivot tables
* Data type conversion

## Data Cleaning

The practice includes:

* Identifying missing values
* Handling missing values
* Removing duplicate records
* Correcting data types
* Removing unnecessary columns
* Renaming columns
* Handling inconsistent data
* Detecting invalid values
* Filtering unwanted records

## Exploratory Data Analysis

The analysis includes:

* Dataset dimensions
* Column information
* Statistical summaries
* Frequency analysis
* Category analysis
* Numerical analysis
* Correlation analysis
* Group-based analysis
* Trend analysis
* Outlier identification

## Practice Projects

The repository includes practical datasets and analytics projects such as:

### Netflix Data Analytics

Analysis of Netflix movies and TV shows using Pandas and NumPy.

### Amazon Sales Analytics

Analysis of Amazon sales data to understand products, sales performance, categories, and trends.

### Microsoft Stock Analytics

Analysis of Microsoft historical stock data including prices, trading volume, and performance trends.

## Project Structure

```text id="i7d0os"
Data-Analytics-Pandas-NumPy/

01_NumPy/
    arrays.py
    indexing.py
    slicing.py
    operations.py
    statistics.py

02_Pandas/
    series.py
    dataframe.py
    filtering.py
    sorting.py
    groupby.py
    merging.py

03_Data_Cleaning/
    missing_values.py
    duplicates.py
    data_types.py
    preprocessing.py

04_Exploratory_Data_Analysis/
    eda.py
    statistical_analysis.py
    correlation.py

05_Projects/
    Netflix_Analytics/
    Amazon_Sales_Analytics/
    Microsoft_Stock_Analytics/

06_Datasets/
    dataset_files

README.md
```

## Daily Practice

For each dataset, I practice:

1. Loading the dataset.
2. Understanding the dataset structure.
3. Checking rows and columns.
4. Checking data types.
5. Identifying missing values.
6. Removing duplicates.
7. Cleaning the data.
8. Filtering required information.
9. Performing calculations.
10. Grouping and aggregating data.
11. Finding trends and patterns.
12. Extracting useful insights.

## Common Pandas Operations

```python
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())

df = df.drop_duplicates()

df["column"].value_counts()

df.groupby("category")["sales"].sum()

df.sort_values("sales", ascending=False)
```

## Common NumPy Operations

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
print(np.sum(data))
```

## Learning Progress

### NumPy

* [x] Arrays
* [x] Indexing
* [x] Slicing
* [x] Array Operations
* [x] Reshaping
* [x] Statistical Functions
* [ ] Broadcasting
* [ ] Matrix Operations

### Pandas

* [x] Series
* [x] DataFrame
* [x] CSV Reading
* [x] Data Inspection
* [x] Filtering
* [x] Sorting
* [x] GroupBy
* [x] Aggregation
* [x] Missing Values
* [x] Duplicate Handling
* [ ] Merging
* [ ] Joining
* [ ] Pivot Tables

### Data Analytics

* [x] Data Cleaning
* [x] Exploratory Data Analysis
* [x] Statistical Analysis
* [x] Data Filtering
* [x] Data Aggregation
* [ ] Advanced EDA
* [ ] Advanced Statistical Analysis

### Projects

* [x] Netflix Data Analytics
* [x] Amazon Sales Analytics
* [x] Microsoft Stock Analytics

## Future Learning

After completing Pandas and NumPy practice, I plan to continue with:

* Matplotlib
* Seaborn
* Advanced Exploratory Data Analysis
* SQL
* Excel
* Power BI
* Statistics for Data Analytics
* Machine Learning

## Purpose

This repository represents my hands-on Data Analytics practice using Python, Pandas, and NumPy.

The main objective is to develop strong data manipulation, data cleaning, exploratory analysis, and problem-solving skills by working with real-world datasets and practical analytics projects.
