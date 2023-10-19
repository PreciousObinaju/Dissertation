import pandas as pd
import os


# List of file paths
file_paths = [
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing 10 twist.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing 20 twist.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 30 backward wing 10 twist.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 30 backward wing.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms bar.csv",
    r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms normal wing.csv",
]

# Create an empty dictionary to store DataFrames
data_frames = {}

# Loop through file paths and read each file into a DataFrame
for file_path in file_paths:
    # Extract the key from the file name (e.g., 'Symmetric wing' from 'Symmetric wing.csv')
    key = file_path.split('\\')[-1].split('.')[0]
    # Read the CSV file into a DataFrame and store it in the dictionary
    data_frames[key] = pd.read_csv(file_path)

bar_df = data_frames['12ms bar']

# Loop through the other DataFrames
for key, df in data_frames.items():
    # Skip the '12ms bar.csv' DataFrame itself
    if key != '12ms bar':
        # Subtract the columns of '12ms bar.csv' from the current DataFrame
        # Assuming the columns have matching names, this will subtract element-wise
        data_frames[key] = df - bar_df

for key, df in data_frames.items():
    if key == '12ms 10 backward wing'or key == '12ms 10 backward wing 20 twist' or key == '12ms 10 backward wing 10 twist' :
        print('12ms 10 backward wing')
        A=0.02969727472
    elif key == '12ms 30 backward wing'or key == '12ms 30 backward wing 10 twist':
        print('12ms 30 backward wing')
        A =0.02364449166

    else:
        print('normalwing')
        A =0.0329868


    column_to_divide = 'Lift(Fz)'
    column_to_divide2 = 'Drag(Fx)'

    # Define the constant divisor
    divisor = 88.2 * (A+ 0.1386+0.0329868)  #

    df['C_L'] = df[column_to_divide] / divisor
    df['C_D'] = df[column_to_divide2] / divisor









output_folder = r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data"
for key, df in data_frames.items():
    # Define the file path for the CSV file in the output folder
    output_file_path = os.path.join(output_folder, f"{key}.csv")
    print(output_file_path)
    # Save the DataFrame to the CSV file
    df.to_csv(output_file_path, index=False)