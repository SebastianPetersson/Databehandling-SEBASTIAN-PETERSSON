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

    plt.figure(figsize=(5,4))
    sns.barplot(x = missing_counts.index, y = missing_counts.values, palette='rocket')
    plt.xlabel('Column')
    plt.ylabel('Amount of missing data')
    plt.tight_layout()

def convert_columns_to_int(df, columns):
    """A tool which converts your column objects to integers.
    columns_to_int(df, columns), set df to your dataframe and a list containing your column names as columns."""

    for column in columns:
        df[column] = (df[column]
                      .astype(str)
                      .str.replace(' ', '', regex = False)
                      .str.replace(',', '.', regex = False)
                      .str.replace('\xa0', '', regex = False)
                      .astype(float)
                      .astype(int))
    return df
    
def convert_columns_to_float(df, columns):
    """A tool which converts your column objects to floats.
    columns_to_float(df, columns), set df to your dataframe and a list containing your column names as columns."""

    for column in columns:
        df[column] = (df[column]
                      .astype(str)
                      .str.replace(' ', '', regex = False)
                      .str.replace(',', '.', regex = False)
                      .str.replace('\xa0', '', regex = False)
                      .astype(float))
    return df