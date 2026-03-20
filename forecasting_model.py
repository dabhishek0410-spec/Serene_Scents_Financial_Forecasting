import pandas as pd
import numpy as np

# Timeline
dates = pd.date_range('2025-07-01', '2026-01-31', freq='D')
df = pd.DataFrame({'date': dates})
n = len(df)

# Demand
trend = np.linspace(10, 130, n)
weekly = 1 + 0.2 * np.sin(2 * np.pi * np.arange(n) / 7)
monthly = 1 + 0.15 * np.sin(2 * np.pi * np.arange(n) / 30)
noise = np.random.normal(0, 5, n)

df['est_units_sold'] = (trend * weekly * monthly + noise).clip(0).round().astype(int)

# Festival boost
df['festival_boost'] = 1.0
for d in ['2025-10-20', '2025-11-01']:
    mask = (
        (df['date'] >= pd.to_datetime(d) - pd.Timedelta(days=3)) &
        (df['date'] <= pd.to_datetime(d) + pd.Timedelta(days=3))
    )
    df.loc[mask, 'festival_boost'] = 1.5

df['est_units_sold'] = (
    df['est_units_sold'] * df['festival_boost']
).round().astype(int).clip(upper=130)

# Pricing & cost
unit_cost = 129.70
price = 195.0

df['est_unit_cost'] = unit_cost
df.loc[df['date'] >= '2025-10-01', 'est_unit_cost'] = unit_cost * 0.85

# Financials
df['est_revenue'] = df['est_units_sold'] * price
df['est_total_cost'] = df['est_units_sold'] * df['est_unit_cost']
df['est_profit'] = df['est_revenue'] - df['est_total_cost']

# Export
df.to_csv('serene_scents_july_realworld.csv', index=False)
