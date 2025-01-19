# Dynamic Golf Caddy System (DGCS) Data Generation Code

This repository contains the data generation scripts for the **Dynamic Golf Caddy System (DGCS)**. The system simulates realistic golfer profiles and their club performances, which can be used for training recommendation algorithms or analyzing golf strategies.

## Features

- **Golfer Profile Simulation**:
  - Generates profiles based on **age**, **handicap (HCP)**, and **gender**.
  - Dynamic assignment of clubs in the bag based on golfer characteristics.
  
- **Realistic Club Distances**:
  - Uses probability distributions to simulate club yardages.
  - Adjusts yardages dynamically for **HCP**, **age**, and **gender**.
  - Includes variability for performance inconsistency.

- **Customizable Bag Selection**:
  - High HCP golfers are more likely to carry hybrids.
  - Low HCP golfers tend to carry fewer hybrids and more irons.
  - Older golfers may prefer hybrids over long irons and may include a 5-Wood.

- **Data Output**:
  - Generates datasets with detailed golfer profiles and club distances.
  - Outputs data as a structured **CSV file** for analysis or training machine learning models.

---

## Installation
1. **Clone the repository**:
```
git clone https://github.com/Aryan-2605/DGCS-Data-Generator.git cd DGCS-Data-Generator
```



2. **Install dependencies**:
Ensure you have Python installed and run:
```
pip install -r requirements.txt yaml Copy code
```

## Usage

### 1. Generate Golfer Data
Run the `Application.py` script to create a dataset:
```
python Application.py
```
By default, the script will:
- Generate profiles for 100 golfers.
- Include clubs and yardages based on dynamic golfer characteristics.

### 2. Customize Data Parameters
You can modify the script to:
- Adjust the number of golfers.
- Change club assignment rules (e.g., hybrid probabilities).
- Update yardage ranges for clubs.

### 3. Output File
The generated data will be saved to a **CSV file** (`golf_dataset.csv`) in the project directory. Example structure:
| ID  | Age | Gender | HCP  | Driver | 3-Wood | 5-Iron | ... |
|------|-----|--------|------|--------|--------|--------|-----|
| 1    | 29  | Male   | 16.1 | 286.5  | 222.9  | 156.3  | ... |
| 2    | 72  | Female | 3.3  | 153.9  | 148.9  | 120.0  | ... |

---

## File Structure

- `Application.py`: Core script to generate the golfer dataset. This is where you can customize the generation. 
- `Operations.py`: contains Important calculations to generate the data set. 
- `data.csv`: Python dependencies for running the script.
- `README.md`: Project documentation.

---

## How It Works

1. **Profile Creation**:
   - Assigns golfers random **age**, **HCP**, and **gender**.
   
2. **Club Selection**:
   - Uses probabilities to assign clubs based on profile characteristics.
   
3. **Yardage Calculation**:
   - Applies realistic yardage ranges and variability using Gaussian distributions.
   - Adjusts yardages for age, gender, and HCP.

4. **CSV Output**:
   - Saves the generated data in a structured format for further analysis.

---

## Customization

### Adjust Number of Golfers
Change the `range` in the loop by configuring the respective variable
### Endless Customization
All elements of this data generator is customizable with the chance of a few values. If you scroll all the way down in the Application.py file you will see the options to customize.

## Example Applications

- **Training Machine Learning Models**:
  - Use the generated dataset to train recommendation systems for club selection.
  
- **Golf Strategy Analysis**:
  - Analyze how age, gender, and HCP influence club selection and performance.

- **Personalized Recommendations**:
  - Enhance golf caddy apps by integrating dynamic datasets.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests. For major changes, please open an issue to discuss the proposed improvements.

---

## License

This project is created by Aryan Gaglani for the purpose of the FYP. 

---
