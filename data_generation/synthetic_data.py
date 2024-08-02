import pandas as pd
import random

# Number of rows
num_rows = 100

# Generate synthetic data
data = {
    'Full Name': [f'Name {i}' for i in range(num_rows)],
    'Date of Birth': [f'Year {random.randint(1900, 2000)}' for _ in range(num_rows)],
    'Social Security Number': [f'{random.randint(100000000, 999999999)}' for _ in range(num_rows)],
    'Address': [f'{random.randint(1, 999)} Random St, City {random.randint(1, 10)}' for _ in range(num_rows)],
    'Phone Number': [f'{random.randint(600000000, 699999999)}' for _ in range(num_rows)],
    'Email Address': [f'email{i}@example.com' for i in range(num_rows)],
    'Bank Name': [f'Bank {random.randint(1, 10)}' for _ in range(num_rows)],
    'Account Number': [f'{random.randint(100000000, 999999999)}' for _ in range(num_rows)],
    'Routing Number': [f'{random.randint(100000000, 999999999)}' for _ in range(num_rows)],
    'Credit Card Number': [f'{random.randint(1000000000000000, 9999999999999999)}' for _ in range(num_rows)],
    'Expiration Date': [f'{random.randint(1, 13)}/25' for _ in range(num_rows)],
    'CVV': [f'{random.randint(100, 999)}' for _ in range(num_rows)],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Add a column for labels: 1 for sensitive, 0 for non-sensitive
# Randomly assign 50% of the rows as sensitive and 50% as non-sensitive
df['IsSensitive'] = random.choices([0, 1], k=num_rows)

# Save to CSV
df.to_csv('C:/MW/pythonProject/data_generation/synthetic_output/synthetic_data.csv', index=False)
