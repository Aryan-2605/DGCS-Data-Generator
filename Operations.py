import random

import numpy as np


class Operations:
    def __init__(self, age, hcp, std, gender):
        self.age = age
        self.hcp = hcp
        self.std = std
        self.gender = gender

    def gen_clubs(self, club_probabilities):
        bag = []
        for club, probability in club_probabilities.items():
            prob = probability(self.age, self.hcp) if callable(probability) else probability
            if random.random() < prob:
                bag.append(club)
        return bag

    def calculate_distance(self, club, male_PGA_yardage, female_PGA_yardage, min_factor, max_factor):
        # Base mean factor from HCP
        mean_factor = min_factor + (max_factor - min_factor) * (36 - min(self.hcp, 36)) / 36

        if self.age > 40:
            age_factor = max(0.5, 1 - (self.age - 40) * 0.01)  # Reduce by 1% per year over 40 capped at 0.7
        else:
            age_factor = 1.0
        mean_factor *= age_factor

        scaling_factor = np.random.normal(loc=mean_factor, scale=self.std)
        scaling_factor = max(min_factor, min(max_factor, scaling_factor))

        # Calculate and return drive distance
        if self.gender == "Male":
            return round(male_PGA_yardage[club] * scaling_factor, 1)
        else:
            return round(female_PGA_yardage[club] * scaling_factor, 1)
