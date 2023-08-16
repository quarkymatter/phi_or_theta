import pandas as pd
import numpy as np
from math import radians, degrees, sin, cos, asin, atan2, acos
import os

# Define the function to perform unit conversions
def convert_units(phi, zenith, azimuth, sidereal_time):
    latitude = radians(40.195203)
    altitude = radians(90 - zenith)
    azimuth_angle = radians(azimuth)
    t = radians(sidereal_time * 15)

    sin_delta = sin(altitude) * sin(latitude) + cos(altitude) * cos(latitude) * cos(azimuth_angle)
    delta = asin(sin_delta)

    cos_H = (sin(altitude) - sin_delta * sin(latitude)) / (cos(delta) * cos(latitude))
    sin_H = (-sin(azimuth_angle) * cos(altitude)) / cos(delta)
    H = atan2(sin_H, cos_H)

    if phi >= 0:
        right_ascension = (2 * np.pi) + (t - H)
    else:
        right_ascension = t - H

    declination = delta

    return degrees(right_ascension), degrees(declination)

# Read the input CSV file
input_file = 'hr1mono_shuf000.xlsx'
output_folder = 'shuffled_results'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Shuffle and process the data 10 times
for shuffle_num in range(1, 11):
    # Shuffle the data
    df = pd.read_excel(input_file)
    df = df.sample(frac=1).reset_index(drop=True)

    # Convert units and create new columns for RA and DEC
    df[['RA', 'DEC']] = df.apply(lambda row: pd.Series(convert_units(row['phi'], row['zen'], row['azi'], row['sid'])), axis=1)

    # Adjust RA values to be in the range [0, 360)
    df['RA'] = (df['RA'] + 360) % 360

    # Filter rows based on 'enc' column condition
    filtered_df = df[df['enc'] > 10 ** 1.4]

    # Perform the energy cut and create the 2D histogram
    ra_values = filtered_df['RA']
    dec_values = filtered_df['DEC']
    ra_bins = np.arange(0, 361, 1)
    dec_bins = np.arange(-90, 91, 1)
    hist, _, _ = np.histogram2d(ra_values, dec_values, bins=[ra_bins, dec_bins])

    # Save the histogram to a CSV file
    output_file = os.path.join(output_folder, f'hr1_shuf{shuffle_num}.csv')
    np.savetxt(output_file, hist, delimiter=',', fmt='%d')
    print(f"Shuffle {shuffle_num} completed. Results saved to '{output_file}'.")
