from scripts.load_data import load_dataset, clean_data
from scripts.analysis import get_summary_stats, compare_sources
from scripts.visualization import plot_summary, plot_scatter
import pandas as pd

# File paths
mcdonalds_file = 'data/mcdonalds.csv'
burger_king_file = 'data/burger_king.csv'

# Load and clean data
mcdonalds_data = clean_data(load_dataset(mcdonalds_file, "McDonald's"))
burger_king_data = clean_data(load_dataset(burger_king_file, "Burger King"))

# Combine datasets
combined_data = pd.concat([mcdonalds_data, burger_king_data], ignore_index=True)

# Analyze data
summary = compare_sources(combined_data)
print("Summary statistics:\n", get_summary_stats(combined_data))
print("Comparison by source:\n", summary)

# Visualize data
plot_summary(summary)
plot_scatter(combined_data, 'Calories', 'Sugars')
