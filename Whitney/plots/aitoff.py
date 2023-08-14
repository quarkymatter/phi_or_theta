import pandas as pd
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np

# Read the filtered CSV file
filtered_file = 'filtered_coordinates.csv'
filtered_df = pd.read_csv(filtered_file)

# Extract RA and DEC columns
ra_values = filtered_df['RA']
dec_values = filtered_df['DEC']

# Create a SkyCoord object with the RA and DEC values
coords = SkyCoord(ra=ra_values * u.degree, dec=dec_values * u.degree, frame='icrs')

# Create a scatter plot with Aitoff projection
plt.figure(figsize=(10, 6))
plt.subplot(111, projection='aitoff')
plt.title('Aitoff Projection of RA vs DEC')
plt.grid(True)

# Convert RA to [-pi, pi] range for Aitoff projection
ra_rad = coords.ra.wrap_at(180 * u.deg).radian

# Plot the points
plt.scatter(ra_rad, coords.dec.radian, s=10, alpha=0.5)

# Show the plot
plt.show()
