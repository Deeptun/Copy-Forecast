import pandas as pd

# Example DataFrames (replace these with your actual data)
# source_df = pd.DataFrame({
#     'Source_SKU': ['SKU1', 'SKU2', 'SKU3'],
#     'Forecast': [100, 120, 150]
# })

source_df = pd.DataFrame({
    'Source_SKU': ['SKU1', 'SKU1', 'SKU1', 'SKU1', 'SKU1', 'SKU1', 'SKU2', 'SKU2', 'SKU2', 'SKU2', 'SKU2', 'SKU2', 'SKU3', 'SKU3', 'SKU3', 'SKU3', 'SKU3', 'SKU3'],
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06',
             '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06',
             '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06'],
    'Forecast': [
        100, 120, 150, 110, 130, 140, 90, 100, 110, 95, 105, 115, 95, 110, 120, 105, 115, 125
    ]
})


mapping_df = pd.DataFrame({
    'Source_SKU': ['SKU1', 'SKU1', 'SKU2', 'SKU3'],
    'Target_SKU': ['SKU4', 'SKU5', 'SKU6', 'SKU7']
})

sku_pairs = [(row['Source_SKU'], row['Target_SKU']) for index, row in mapping_df.iterrows()]

# Print the generated SKU pairs list
print("SKU pairs:")
print(sku_pairs)

# def copy_forecast(source_sku, target_sku, forecast_data):
#     if source_sku in forecast_data and target_sku in forecast_data:
#         forecast_data[target_sku] = forecast_data[source_sku]
#         print(f"Forecast copied from {source_sku} to {target_sku}")
#     else:
#         print("Source or target SKU not found in forecast data")

# Loop through the SKU pairs and copy forecasts

Target_forecast = pd.DataFrame()
for source_sku, target_sku in sku_pairs:
    forecast_values = source_df[source_df['Source_SKU'] == source_sku]
    forecast_values["Target_SKU"] = target_sku
    Target_forecast = pd.concat([Target_forecast,forecast_values],ignore_index=True)
    # copy_forecast(source_sku, target_sku, source_df)
print("\nUpdated forecast data:")
print(source_df)
print(Target_forecast)
# Print the updated forecast data after copying forecasts
# print("Updated forecast data:")
# for sku, forecast in source_df.items():
#     print(f"SKU: {sku}, Forecast: {forecast}")

'''
Target_forecast = pd.DataFrame()
# Double for loop to copy forecast from base SKU to target SKU
for base_sku in mapping_df['Source_SKU'].unique().tolist():
    for target_sku in mapping_df['Target_SKU'].unique().tolist():
        forecast_values = source_df[source_df['Source_SKU'] == base_sku]
        forecast_values["Target_SKU"] = target_sku
        Target_forecast = pd.concat([Target_forecast,forecast_values],ignore_index=True)
        print(f"Forecast copied from {base_sku} to {target_sku}")

print("\nUpdated Mapping DataFrame:")
print(Target_forecast)
'''


