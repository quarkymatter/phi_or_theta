import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os

# Read the shuffled CSV files
shuffled_folder = r"C:\Users\whitn\OneDrive\Desktop\shuffled_results"
shuffled_files = [f for f in os.listdir(shuffled_folder) if f.startswith('hr1_shuf')]


# Initialize the combined histogram
combined_hist = np.zeros((360, 180))

# Aggregate histograms from all shuffled files
for shuffled_file in shuffled_files:
    hist = np.loadtxt(os.path.join(shuffled_folder, shuffled_file), delimiter=',')
    combined_hist += hist  # Adjust dimensions to match combined_hist

# Create a figure and axis with Aitoff projection
fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(111, projection=ccrs.Aitoff())

# Plot the heat map
ra_bins = np.arange(-1, 361, 1)
dec_bins = np.arange(-91, 91, 1)
ra_centers = (ra_bins[:-1] + ra_bins[1:]) / 2
dec_centers = (dec_bins[:-1] + dec_bins[1:]) / 2
ra_mesh, dec_mesh = np.meshgrid(np.radians(ra_centers), np.radians(dec_centers))

plt.pcolormesh(ra_mesh, dec_mesh, combined_hist.T, cmap='plasma', shading='auto')
plt.colorbar(label='Number of Events')

# Add gridlines
ax.gridlines()

# Set title and labels
plt.title('Aitoff Projection Heat Map (Shuffled Data)')
plt.xlabel('Right Ascension (RA)')
plt.ylabel('Declination (DEC)')

# Show the plot
plt.show()
