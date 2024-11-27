def get_summary_stats(df):
    """Returns summary statistics for the dataset."""
    return df.describe()

def compare_sources(df):
    """Compares average nutritional values by source."""
    return df.groupby('Source').mean()
