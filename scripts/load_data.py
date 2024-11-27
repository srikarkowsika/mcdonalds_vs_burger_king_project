import pandas as pd

def load_dataset(file_path):
    """Loads a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

def clean_data(df, source):
    """Cleans and standardizes the dataset."""
    df = df[['Item', 'Category', 'Calories', 'Fat (g)', 'Sodium (mg)', 'Sugars (g)', 'Dietary Fiber (g)', 'Protein (g)']]
    df['Source'] = source
    return df
