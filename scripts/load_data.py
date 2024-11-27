import pandas as pd

def load_dataset(file_path, source):

    """
    Loads a CSV file into a pandas DataFrame and adds a source column.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    - source (str): Source name (e.g., "McDonald's" or "Burger King").

    Returns:
    - pd.DataFrame: Cleaned DataFrame with a Source column added
    
    """
    try:
        df = pd.read_csv(file_path)
        df['Source'] = source
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def clean_data(df):
    """
    Cleans the DataFrame by renaming columns and handling missing values.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.

    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    """
    # Example renaming of columns (customize based on your dataset)
    df = df.rename(columns={
        'Calories': 'Calories',
        'Fat (g)': 'Fat',
        'Sodium (mg)': 'Sodium',
        'Sugars (g)': 'Sugars',
        'Dietary Fiber (g)': 'Fiber',
        'Protein (g)': 'Protein'
    })
    return df
