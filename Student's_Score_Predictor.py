#Based_on_Linear_Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 
print("Loading data...")
df = pd.read_csv('student_scores.csv')
print(df.head())

# 2. Visualize the data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Hours', y='Scores')
plt.title('Hours Studied vs Percentage Score')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.grid(True)
plt.savefig('initial_plot.png')
print("Initial plot saved as 'initial_plot.png'")

# 3. Prepare the data
X = df.iloc[:, :-1].values  # Features (Hours)
y = df.iloc[:, 1].values    # Target (Scores)

# Split into Training and Testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 4. Train the Model
print("\nTraining the Linear Regression model...")
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Training complete.")

# 5. Plotting the Regression Line
line = regressor.coef_ * X + regressor.intercept_

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, line, color='red', label='Regression Line')
plt.title('Regression Line: Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.legend()
plt.grid(True)
plt.savefig('regression_result.png')
print("Regression plot saved as 'regression_result.png'")

# 6. Making Predictions
print("\nMaking predictions on test data...")
y_pred = regressor.predict(X_test)

# Comparing Actual vs Predicted
df_compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nComparison of Actual vs Predicted:")
print(df_compare)

# 7. Model Evaluation
print("\nModel Evaluation:")
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('R-squared Score:', metrics.r2_score(y_test, y_pred))

# 8. Custom Prediction
hours = float(input("Enter the number of hours you want to study daily : "))
own_pred = regressor.predict([[hours]])
print(f"\nPredicted Score for {hours} hours/day: {own_pred[0]:.2f}%")

