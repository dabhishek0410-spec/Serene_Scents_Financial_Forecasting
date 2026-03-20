import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Timeline
date_rng = pd.date_range(start='2025-07-01', end='2026-01-31', freq='D')
forecast_df = pd.DataFrame(date_rng, columns=['date'])
n_days = len(forecast_df)

# Demand generation
trend = np.linspace(10, 130, n_days)
weekly = 1 + 0.2 * np.sin(2 * np.pi * np.arange(n_days) / 7)
monthly = 1 + 0.15 * np.sin(2 * np.pi * np.arange(n_days) / 30)
noise = np.random.normal(0, 5, n_days)

forecast_df['est_units_sold'] = (trend * weekly * monthly + noise).clip(0).round().astype(int)

# Festival boost
festival_dates = ['2025-10-20', '2025-11-01']
forecast_df['festival_boost'] = 1.0

for date in festival_dates:
    mask = (
        (forecast_df['date'] >= pd.to_datetime(date) - pd.Timedelta(days=3)) &
        (forecast_df['date'] <= pd.to_datetime(date) + pd.Timedelta(days=3))
    )
    forecast_df.loc[mask, 'festival_boost'] = 1.5

forecast_df['est_units_sold'] = (
    forecast_df['est_units_sold'] * forecast_df['festival_boost']
).round().astype(int).clip(upper=130)

# Pricing and cost
unit_cost_initial = 129.70
selling_price = 195.0

forecast_df['est_unit_cost'] = unit_cost_initial
forecast_df.loc[forecast_df['date'] >= '2025-10-01', 'est_unit_cost'] = unit_cost_initial * 0.85

# Financials
forecast_df['est_revenue'] = forecast_df['est_units_sold'] * selling_price
forecast_df['est_total_cost'] = forecast_df['est_units_sold'] * forecast_df['est_unit_cost']
forecast_df['est_profit'] = forecast_df['est_revenue'] - forecast_df['est_total_cost']

# Volatility
np.random.seed(42)
volatility = np.random.normal(0, 0.08, n_days)
forecast_df['est_units_sold'] = (
    forecast_df['est_units_sold'] * (1 + volatility)
).clip(lower=0).round().astype(int)

# Delays
delay_flag = np.random.choice([0, 1], size=n_days, p=[0.95, 0.05])
forecast_df['delay_flag'] = delay_flag

forecast_df['est_units_sold'] = np.where(
    forecast_df['delay_flag'] == 1,
    forecast_df['est_units_sold'] * 0.7,
    forecast_df['est_units_sold']
).round().astype(int)

# Recalculate financials
forecast_df['est_revenue'] = forecast_df['est_units_sold'] * selling_price
forecast_df['est_total_cost'] = forecast_df['est_units_sold'] * forecast_df['est_unit_cost']
forecast_df['est_profit'] = forecast_df['est_revenue'] - forecast_df['est_total_cost']

# Summary
total_revenue = forecast_df['est_revenue'].sum()
total_profit = forecast_df['est_profit'].sum()
avg_margin = (forecast_df['est_profit'] / forecast_df['est_revenue']).mean()

print("\n📊 BUSINESS SUMMARY")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Average Profit Margin: {avg_margin:.2%}")

best_day = forecast_df.loc[forecast_df['est_profit'].idxmax()]
worst_day = forecast_df.loc[forecast_df['est_profit'].idxmin()]

print("\n🏆 Best Day:", best_day['date'], "| Profit:", best_day['est_profit'])
print("⚠️ Worst Day:", worst_day['date'], "| Profit:", worst_day['est_profit'])

# Visualization
plt.figure(figsize=(12, 6))
plt.plot(forecast_df['date'], forecast_df['est_revenue'], label='Revenue')
plt.plot(forecast_df['date'], forecast_df['est_profit'], label='Profit')

plt.title("Serene Scents Forecast")
plt.xlabel("Date")
plt.ylabel("₹ Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
