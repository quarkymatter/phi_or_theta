import pandas as pd
import numpy as np
from math import radians, degrees, sin, cos, acos, asin, atan2

# Define the function to perform unit conversions
def convert_units(phi, zenith, azimuth, sidereal_time):
    latitude = radians(40.195203)
    altitude = radians(90 - zenith)
    azimuth_angle = radians(azimuth)
    t = radians(sidereal_time*15)

    sin_delta = sin(altitude) * sin(latitude) + cos(altitude) * cos(latitude) * cos(azimuth_angle)
    delta = asin(sin_delta)
    
    

    cos_H = (sin(altitude) - sin_delta * sin(latitude)) / (cos(delta) * cos(latitude))
    sin_H = ((-sin(azimuth_angle)) * cos(altitude)) / cos(delta)
    H_cos = acos(cos_H)
    H_sin = asin(sin_H)
    
    H = atan2(sin_H, cos_H)

    
    
    if phi>=0:
         right_ascension = (2*np.pi)+(t - H)
    elif phi<0:
        right_ascension = t - H
        
    declination = delta

    return degrees(right_ascension), degrees(declination)

# Read the input CSV file
input_file = 'hr1mono_shuf000.xlsx'
df = pd.read_excel(input_file)

# Convert units and create new columns for RA and DEC
df[['RA', 'DEC']] = df.apply(lambda row: pd.Series(convert_units(row['phi'], row['zen'], row['azi'], row['sid'])), axis=1)

# Write the modified DataFrame to a new CSV file
output_file = 'converted_coord.csv'
df.to_csv(output_file, index=False)

print(f"Conversion completed. Results saved to '{output_file}'.")
