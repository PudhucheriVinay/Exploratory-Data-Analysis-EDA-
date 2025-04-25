# Titanic EDA Project

This project contains an exploratory data analysis (EDA) of the Titanic dataset.

## Files

- `titanic_eda.py`: Python script performing EDA including summary statistics, histograms, boxplots, pairplots, and correlation heatmap for numeric features.
- `titanic_cleaned.csv`: Cleaned Titanic dataset used for the analysis.

## Description

The script loads the Titanic dataset, prints summary statistics, and visualizes the data distributions and relationships among numeric features using seaborn and matplotlib.

## How to Run

1. Ensure you have Python installed with the required packages: pandas, matplotlib, seaborn.
2. Run the script using:
   ```
   python titanic_eda.py
   ```
3. The script will output summary statistics and display various plots for data exploration.

## Notes

- The dataset file `titanic_cleaned.csv` must be in the same directory as the script.
- This project is intended for data exploration and visualization purposes.

## Interview Questions & Answers

1. What is the purpose of EDA?
To understand the structure, trends, anomalies, and relationships in data before modeling.

2. How do boxplots help in understanding a dataset?
They show the distribution, median, quartiles, and outliers in numeric data.

3. What is correlation and why is it useful?
It's a measure of relationship strength between variables—important for feature selection.

4. How do you detect skewness in data?
Using .skew() or histograms—positive/negative skew indicates imbalance.

5. What is multicollinearity?
When independent features are highly correlated, which can distort model accuracy.

6. What tools do you use for EDA?
Pandas, Seaborn, Matplotlib, Plotly, and sometimes Sweetviz or Pandas Profiling.

7. Can you explain a time when EDA helped you find a problem?
Example: Found class imbalance in a customer churn dataset using barplots—guided resampling decisions.

8. What is the role of visualization in ML?
To reveal hidden patterns, guide feature engineering, and communicate insights clearly.

