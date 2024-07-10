import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load your dataset
data_path = 'data\\diet_dataset.csv'  # Replace with the actual path to your dataset
df = pd.read_csv(data_path)

# Prepare the data
X = df[['age', 'height', 'weight', 'gender']]
y = df['calories_to_maintain_weight']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'calorie_model.pkl')
