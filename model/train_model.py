import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load the preprocessed data
data = pd.read_csv('processed_data.csv')

# Define features (independent variables) and target (dependent variable)
X = data[['Humidity', 'Wind Speed', 'Weather Condition']]  # Replace with actual column names
y = data['Temperature']  # Replace with the column name for temperature

# One-Hot Encode the Weather Condition column
X = pd.get_dummies(X, columns=['Weather Condition'], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model as a pickle file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as 'model.pkl'")
