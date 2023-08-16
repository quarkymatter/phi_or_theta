import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Read the filtered CSV file
filtered_file = r"C:\Users\whitn\OneDrive\Desktop\energy_cut_19.4.csv"
filtered_df = pd.read_csv(filtered_file)

# Extract RA and DEC columns
ra_values = filtered_df['RA']
dec_values = filtered_df['DEC']

# Create a figure and axis with Aitoff projection
fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(111, projection=ccrs.Aitoff())

# Plot the heat map
hist, xedges, yedges = np.histogram2d(ra_values, dec_values, bins=100)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(hist.T, origin='lower', extent=extent, cmap='plasma', aspect='auto')

# Add gridlines
ax.gridlines()

# Set title and labels
plt.title('Aitoff Projection Heat Map')
plt.xlabel('Right Ascension (RA)')
plt.ylabel('Declination (DEC)')

# Show the color bar
cbar = plt.colorbar(label='Number of Events')

# Show the plot
plt.show()

