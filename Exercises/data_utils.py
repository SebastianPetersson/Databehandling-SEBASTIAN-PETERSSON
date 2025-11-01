import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_missing_values(df):
    """Plots the amount of missing values per column in a DataFrame, as a barplot.\n Only columns with missing values are gonna show up."""

    sns.set_theme(style = 'darkgrid')

    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0]

    # if missing_counts.empty:
    #     print('No values are missing in this column: {df.column}')
    #     return

    plt.figure(figsize=(8,6))
    sns.barplot(x = missing_counts.index, y = missing_counts.values, palette='rocket')
    plt.xlabel('Column')
    plt.ylabel('Amount of missing data')
    plt.tight_layout()

