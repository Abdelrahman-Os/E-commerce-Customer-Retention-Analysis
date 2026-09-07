import pandas as pd
import numpy as np

np.random.seed(42)
n_orders = 1000

data = {
    'OrderID': range(1001, 1001 + n_orders),
    'CustomerID': np.random.randint(500, 600, size=n_orders),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home & Kitchen', 'Books'], size=n_orders),
    'Sales': np.random.uniform(10, 500, size=n_orders).round(2),
    'Quantity': np.random.randint(1, 5, size=n_orders),
    'DaysSinceLastPurchase': np.random.randint(1, 180, size=n_orders),
    'Satisfied': np.random.choice([0, 1], size=n_orders, p=[0.2, 0.8])
}

df = pd.DataFrame(data)
df.to_csv('ecommerce_data.csv', index=False)