import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01'],
    'Income': [5000, 6000, 5500, 7000],
    'Expenses': [4000, 4500, 4000, 6500],
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' to datetime format

# Plotting
plt.figure(figsize=(6,3))
plt.plot(df['Date'], df['Income'], label='Income', marker='o')
plt.plot(df['Date'], df['Expenses'], label='Expenses', marker='o')
plt.title('Personal Finance Dashboard')
plt.xlabel('Date')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()
