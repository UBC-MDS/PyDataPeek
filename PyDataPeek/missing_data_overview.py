import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from xlrd import XLRDError


def _read_file(file, sheet_name=0):
    """Helper function used to read the file and return a pandas dataframe.

    Checks if file type is a .csv or excel. If not, returns a ValueError.

    Parameters
    ----------
    file : str
        the name of the file, including the filetype extension
    sheet_name : int, optional
        if passing an excel file, the name of the sheet to analyze,
        by default 0

    Returns
    -------
    pandas.Dataframe
        pandas dataframe containing data from file
    """
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        try:
            df = pd.read_excel(file, sheet_name=sheet_name)
        except XLRDError:
            raise ValueError("Please use a valid csv or excel file.")
    return df


def _make_plot(df):
    """Helper function used to create heatmap showing missing values in
    a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        the dataframe object to analyze

    Returns
    -------
    matplotlib figure
        a matplotlib heatmap figure
    """
    fig = plt.figure(figsize=(40, 20))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.ylabel("Row number", fontsize=25)
    plt.xlabel("Column name", fontsize=25)
    plt.title("Heatmap of missing values", fontsize=30)
    plt.tick_params(labelsize=20)
    return fig
