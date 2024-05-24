import pandas as pd

# Load historical expense data
data = pd.read_csv('expenses.csv')

# Feature engineering
data['year'] = pd.to_datetime(data['date']).dt.year

# Save preprocessed data
data.to_csv('preprocessed_expenses.csv', index=False)
