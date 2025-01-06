import pandas as pd

from Operations import *


class Application:
    def __init__(self, age_rdm, hcp_rdm, std_rdm, gender_rdm, data_points, column_order, club_probabilities,
                 male_PGA_yardage, female_PGA_yardage, min_factor, max_factor):
        self.age_rdm = age_rdm
        self.hcp_rdm = hcp_rdm
        self.std_rdm = std_rdm
        self.gender_rdm = gender_rdm
        self.data_points = data_points + 1
        self.column_order = column_order
        self.club_probabilities = club_probabilities
        self.male_PGA_yardage = male_PGA_yardage
        self.female_PGA_yardage = female_PGA_yardage
        self.min_factor = min_factor
        self.max_factor = max_factor

    def run(self):
        data = []
        for i in range(1, self.data_points):
            age = self.age_rdm()
            hcp = self.hcp_rdm()
            std = self.std_rdm(hcp)
            gender = self.gender_rdm()
            golfer = Operations(age, hcp, std, gender)
            clubs = golfer.gen_clubs(self.club_probabilities)
            golfer_data = {'ID': i, 'Age': age, 'Gender': gender, 'HCP': hcp}

            for club in clubs:
                golfer_data[club] = golfer.calculate_distance(club, self.male_PGA_yardage, self.female_PGA_yardage,
                                                              self.min_factor, self.max_factor)
            data.append(golfer_data)

        df = pd.DataFrame(data)
        for col in self.column_order:
            if col not in df.columns:
                df[col] = np.nan

        df = df[self.column_order]
        print(df.head())
        df.to_csv('data.csv', index=False)


if __name__ == '__main__':
    #Modify Age Randomization
    age = lambda: np.random.randint(18, 80)

    #Modify HCP Randomization
    hcp = lambda: round(np.random.uniform(0, 36), 1)

    #Modifiy Standard Deviation Randomization
    std = lambda hcp: round(np.random.uniform(0, 0.05), 2) if hcp < 10 else round(np.random.uniform(0.04, 0.09), 2)

    #Modify Gender Randomization
    gender = lambda: "Male" if np.random.random() < 0.65 else "Female"

    #Order of the columns in the data.csv file
    column_order = ['ID', 'Age', 'Gender', 'HCP', 'Driver', '3-Wood', '5-Wood', '3-Hybrid', '4-Hybrid', '5-Hybrid',
                    '4-Iron', '5-Iron', '6-Iron', '7-Iron', '8-Iron', '9-Iron', 'PW', 'GW', 'SW', 'LW']

    #Number of generated entries
    data_points = 500

    #Min factor
    min_factor = 0.50
    #Max Factor
    max_factor = 1.08

    #Modify the golfers bag
    club_probabilities = {
        'Driver': 1.0,
        '3-Wood': lambda age, hcp: 0.9 if hcp < 25 else 0.5,
        '5-Wood': lambda age, hcp: max(0.4 if age > 50 else 0.1, 0.3 if hcp < 10 else 0.1),
        '3-Hybrid': lambda age, hcp: 0.1 if hcp > 15 else 0.5,
        '4-Hybrid': lambda age, hcp: 0.1 if hcp > 10 else 0.2,
        '5-Hybrid': lambda age, hcp: 0.5 if hcp > 15 else 0.2,
        '4-Iron': lambda age, hcp: 0.1 if hcp > 10 else 0.5,
        '5-Iron': lambda age, hcp: 0.3 if hcp > 10 else 0.9,
        '6-Iron': lambda age, hcp: 0.9,
        '7-Iron': lambda age, hcp: 0.95,
        '8-Iron': lambda age, hcp: 0.95,
        '9-Iron': lambda age, hcp: 0.95,
        'PW': lambda age, hcp: 1.0,
        'GW': lambda age, hcp: 0.5,
        'SW': lambda age, hcp: 1.0,
        'LW': lambda age, hcp: 0.5,
    }

    #Modify base male yardages (These are sources from the PGA website)
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

    #Modify base female yardages (These are sources from the PGA website)
    female_PGA_yardage = {'Driver': 223,
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

    App = Application(age, hcp, std, gender, data_points, column_order, club_probabilities, male_PGA_yardage,
                      female_PGA_yardage, min_factor, max_factor)
    App.run()
