import pandas as pd
import numpy as np
import random as rd
import datetime as dt

clubs = {'Woods': ['Driver', '3-Wood', '5-Wood'],
         'Hybrids': ['3-Hybrid', '4-Hybrid', '5-Hybrid'],
         'Irons': ['4-Iron', '5-Iron', '6-Iron', '7-Iron', '8-Iron', '9-Iron'],
         'Wedges': ['PW', 'GW', 'SW', 'LW']}

male_PGA_yardage = {'Driver': 281.6,
                    '3-Wood': 249,
                    '5-Wood': 236,
                    '3-Hybrid': 222,
                    '4-Hybrid': 213,
                    '5-Hybrid': 200,
                    '4-Iron': 209,
                    '5-Iron': 199,
                    '6-Iron': 188,
                    '7-Iron': 176,
                    '8-Iron': 164,
                    '9-Iron': 152,
                    'PW': 142,
                    'GW': 132,
                    'SW': 121,
                    'LW': 110

                    }

Female_PGA_yardage = {'Driver': 223,
                      '3-Wood': 200,
                      '5-Wood': 189,
                      '3-Hybrid': 178,
                      '4-Hybrid': 170,
                      '5-Hybrid': 160,
                      '4-Iron': 175,
                      '5-Iron': 166,
                      '6-Iron': 155,
                      '7-Iron': 143,
                      '8-Iron': 133,
                      '9-Iron': 123,
                      'PW': 111,
                      'GW': 105,
                      'SW': 97,
                      'LW': 90,
                      }
def male_drive_distance(age, club, hcp, std_dev, min_factor=0.50, max_factor=1.08):
    # Base mean factor from HCP
    mean_factor = min_factor + (max_factor - min_factor) * (36 - min(hcp, 36)) / 36

    if age > 40:
        age_factor = max(0.5, 1 - (age - 40) * 0.01)  # Reduce by 1% per year over 40 capped at 0.7
    else:
        age_factor = 1.0
    mean_factor *= age_factor

    # Log for debugging
  #  print(f"Age: {age}, HCP: {hcp}, Mean Factor: {mean_factor}")

    # Generate scaling factor with adjusted mean
    scaling_factor = np.random.normal(loc=mean_factor, scale=std_dev)
    scaling_factor = max(min_factor, min(max_factor, scaling_factor))

    # Calculate and return drive distance
    return round(male_PGA_yardage[club] * scaling_factor, 1)


for item in male_PGA_yardage.keys():
    drive_distance = male_drive_distance(20, item, 1, std_dev=0.04)
    print(f'{item}: {drive_distance}')