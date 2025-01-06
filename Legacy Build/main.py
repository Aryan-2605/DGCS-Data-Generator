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
def calculate_distance(age, club, hcp, std_dev, gender, min_factor=0.50, max_factor=1.08):
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
    if gender == "Male":
        return round(male_PGA_yardage[club] * scaling_factor, 1)
    else:
        return round(Female_PGA_yardage[club] * scaling_factor, 1)


for item in male_PGA_yardage.keys():
    drive_distance = calculate_distance(20, item, 1, std_dev=0.04, gender="Male")
    print(f'{item}: {drive_distance}')


def select_clubs(age, hcp):
    clubs =[]
    club_probabilities = {
        'Driver': 1,
        '3-Wood': 0.9 if hcp < 25 else 0.5,
        '5-Wood': max(0.4 if age > 50 else 0.1, 0.3 if hcp < 10 else 0.1),
        '3-Hybrid': 0.1 if hcp > 15 else 0.5,
        '4-Hybrid': 0.1 if hcp > 10 else 0.2,
        '5-Hybrid': 0.5 if hcp > 15 else 0.2,
        '4-Iron': 0.1 if hcp > 10 else 0.5,
        '5-Iron': 0.3 if hcp > 10 else 0.9,
        '6-Iron': 0.9,
        '7-Iron': 0.95,
        '8-Iron': 0.95,
        '9-Iron': 0.95,
        'PW': 1,
        'GW': 0.5,
        'SW': 1,
        'LW': 0.5
    }
    for club, probability in club_probabilities.items():
        if np.random.rand() < probability:
            clubs.append(club)
    return clubs

print(select_clubs(20, 1))

column_order = ['ID', 'Age', 'Gender', 'HCP', 'Driver', '3-Wood', '5-Wood', '3-Hybrid', '4-Hybrid', '5-Hybrid',
                '4-Iron', '5-Iron', '6-Iron', '7-Iron', '8-Iron', '9-Iron', 'PW', 'GW', 'SW', 'LW']

data = []
for i in range(1,1001):
    age = np.random.randint(18, 80)
    hcp = round(np.random.uniform(0, 36),1)
    std = round(np.random.uniform(0, 0.05),2) if hcp < 10 else round(np.random.uniform(0.04, 0.09),2)
    gender = "Male" if np.random.random() < 0.65 else "Female"
    golfer_data = {'ID': i, 'Age': age, 'Gender': gender, 'HCP': hcp}
    clubs = select_clubs(age, hcp)
    for club in clubs:
        golfer_data[club] = calculate_distance(age, club, hcp, std, gender)
    #print(golfer_data)
    data.append(golfer_data)
df = pd.DataFrame(data)
df = df[column_order]
print(df.head())
df.to_csv('data.csv')

