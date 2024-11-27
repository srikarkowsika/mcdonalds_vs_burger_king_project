import matplotlib.pyplot as plt
import seaborn as sns

def plot_summary(summary_df):
    """Plots a bar chart of average nutritional values."""
    summary_df.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Nutritional Values: McDonald\'s vs Burger King')
    plt.xlabel('Metrics')
    plt.ylabel('Average Value')
    plt.show()
