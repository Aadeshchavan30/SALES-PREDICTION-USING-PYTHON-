import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
file_path = '/content/Advertising.csv'  # Replace with the correct path to your file
data = pd.read_csv('/content/Advertising.csv')

# Remove the 'Unnamed: 0' column
data = data.drop(columns=['Unnamed: 0'])

# Display basic statistics of the dataset
print(data.describe())

# Set the style of the visualization
sns.set(style="ticks", color_codes=True)

# Create scatter plots for each feature against the target variable
plt.figure(figsize=(15, 5))

# TV vs Sales
plt.subplot(1, 3, 1)
sns.scatterplot(data=data, x='TV', y='Sales')
plt.title('TV vs Sales')

# Radio vs Sales
plt.subplot(1, 3, 2)
sns.scatterplot(data=data, x='Radio', y='Sales')
plt.title('Radio vs Sales')

# Newspaper vs Sales
plt.subplot(1, 3, 3)
sns.scatterplot(data=data, x='Newspaper', y='Sales')
plt.title('Newspaper vs Sales')

plt.tight_layout()
plt.show()

# Define features and target variable
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
