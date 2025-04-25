import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('titanic_cleaned.csv')

# 1. Summary statistics
summary_stats = df.describe(include='all')
print("Summary Statistics:")
print(summary_stats)

# 2. Histograms and boxplots for numeric features
numeric_features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

for feature in numeric_features:
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df[feature], kde=True)
    plt.title(f'Histogram of {feature}')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
    
    plt.tight_layout()
    plt.show()

# 3. Pairplot and correlation matrix for feature relationships
sns.pairplot(df[numeric_features])
plt.suptitle('Pairplot of Numeric Features', y=1.02)
plt.show()

corr_matrix = df[numeric_features].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# 4. Identify patterns, trends, or anomalies in the data
# This will be done visually through the plots above.

# 5. Basic feature-level inferences from visuals
# User can interpret from the printed summary statistics and plots.
