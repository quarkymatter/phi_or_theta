 pandas as pd
import matplotlib.pyplot as plt

# Read the filtered CSV file
filtered_file = 'energy_cut_10**19.4.csv'
filtered_df = pd.read_csv(filtered_file)

# Extract RA and DEC columns
ra_values = filtered_df['RA']
dec_values = filtered_df['DEC']

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(ra_values, dec_values, s=10, alpha=0.5,color='red')
plt.xlabel('Right Ascension (deg)')
plt.ylabel('Declination (deg)')
plt.title('Scatter Plot of RA vs DEC')
plt.show()
