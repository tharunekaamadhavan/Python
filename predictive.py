import pandas as pd

# Load the data
data_path = 'inventoryy.csv'
df = pd.read_csv(data_path)

# Display basic information and the first few rows
print(df.info())
print(df.head())
# Check for missing values
print(df.isnull().sum())

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract date-based features
df['year'] = df['Timestamp'].dt.year
df['month'] = df['Timestamp'].dt.month
df['day'] = df['Timestamp'].dt.day
df['weekday'] = df['Timestamp'].dt.weekday
df['hour'] = df['Timestamp'].dt.hour

# Drop 'Date' column as it is redundant with 'Timestamp'
df.drop(columns=['Date'], inplace=True)

# Fill missing values
df.ffill(inplace=True)
# Ensure 'Quantity' column exists for creating lag features
df['lag_1'] = df['Quantity'].shift(1)
df['lag_7'] = df['Quantity'].shift(7)
df['lag_30'] = df['Quantity'].shift(30)
df.dropna(inplace=True)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Define features and target
features = ['Price', 'Ratings', 'year', 'month', 'day', 'weekday', 'hour', 'lag_1', 'lag_7', 'lag_30']
target = 'Quantity'

X = df[features]
y = df[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')
# Further evaluation metrics
from sklearn.metrics import r2_score, mean_squared_error

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'R^2 Score: {r2}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')

# Hyperparameter tuning (example using GridSearchCV)
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(model, param_grid, cv=3, scoring='neg_mean_absolute_error')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
best_params = grid_search.best_params_
print(f'Best Parameters: {best_params}')

# Predict with the best model
y_pred_best = best_model.predict(X_test)
mae_best = mean_absolute_error(y_test, y_pred_best)
print(f'Best Model Mean Absolute Error: {mae_best}')
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Save the trained model
joblib.dump(best_model, 'best_model.pkl')

# Load the trained model
model = joblib.load('best_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = pd.DataFrame(data, index=[0])
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
import requests

url = 'http://localhost:5000/predict'
data = {
    'Price': 10.99,
    'Ratings': 4.5,
    'year': 2024,
    'month': 5,
    'day': 23,
    'weekday': 2,
    'hour': 14,
    'lag_1': 20,
    'lag_7': 30,
    'lag_30': 25
}

response = requests.post(url, json=data)
print(response.json())

