import pandas as pd

def load_data(filename):
    # Load the dataset
    file_path = 'path_to_your_file.txt'  # Replace with the actual path to your file
    df = pd.read_csv(file_path, delimiter='|')

    # Display the first few rows of the DataFrame
    print(df.head())
