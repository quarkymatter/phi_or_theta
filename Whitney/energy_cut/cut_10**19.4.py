import pandas as pd
import numpy as np
from math import radians, degrees, sin, cos, asin, atan2

# Read the input xlsx file
input_file = 'hr1mono_shuf000.xlsx'
df = pd.read_excel(input_file)


# Adjust RA values to be in the range [0, 360)
df['RA'] = (df['RA'] + 360) % 360

# Filter rows based on 'enc' column condition
filtered_df = df[df['enc'] > 10 ** 1.4]

# Write the filtered DataFrame to a new CSV file
output_file = 'energy_cut_10**19.4.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Filtering completed. Filtered results saved to '{output_file}'.")
