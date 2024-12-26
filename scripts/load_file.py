import pandas as pd

def load_data(filename):
    # Load the dataset
    file_path = '../data/raw/MachineLearningRating_v3.txt'  # Replace with the actual path to your file
    df = pd.read_csv(file_path, delimiter='|')

    # Display the first few rows of the DataFrame
    return df