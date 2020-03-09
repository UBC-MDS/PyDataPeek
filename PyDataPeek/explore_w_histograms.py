import pandas as pd
import altair as alt
from altair_saver import save


def read_file(file, sheet_name=0):
    """
    Helper function used to read the file and return a pandas dataframe.
    Checks if file type is a .csv or excel. If not, returns a ValueError.
    Parameters
    ----------
    file : str
        the name of the file, including the filetype extension
    sheet_name : int, optional
        if passing an excel file, the name of the sheet to analyze, by default 0
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
        except:
            raise ValueError("Please use a valid csv or excel file.")
    return df


def is_numeric(df, column):
    """
    Helper function used to take a dataframe, a column name
    Returns True if the column is numerical, False otherwise

    Parameters
    --------
    file:
        a csv file
    column: 
        a column name as a string


    Returns
    -------
    Bool
    """

    if str(df[column].dtypes) == 'int64' or str(df[column].dtypes) == 'float64':
        return True
    else:
        return False


def make_save_histogram(df, column):
    """
    Helper function used to take a dataframe, a numerical column name, 
    and returns a png file of histogram(s)

    Parameters
    --------
    file:
        a csv file
    column: 
        a numerical column name as a string


    Returns
    -------
    .png file of histogram
    """

    # plot and save the chart with different name
    chart = alt.Chart(df).mark_bar().encode(
        alt.X(column+':Q', bin=True),
        alt.Y('count()')
    )

    chart.save(column + '_chart' + '.png')


def explore_w_histograms(file, columns_list=[], sheet_name=0):
    """
    take a csv file, a sheet name (default 0),
    a list of numerical column names 
    and returns a png file of histogram(s)

    Parameters
    --------
    file:
        a csv file
    columns_list: 
        a list of numerical column names as strings, default = []


    Returns
    -------
    .png file(s) of histogram(s)

    Example
    -------
    >>> explore_w_histograms('data/toy_dataset.csv', ['volumn', 'date'])
    """
    df = read_file(file, sheet_name=0)

    try:
        column = columns_list[0]
    except:
        raise ValueError("Make sure column name is in your data!")

    for i in range(0, len(columns_list)):
        if is_numeric(df, columns_list[i]) == True:
            make_save_histogram(df, columns_list[i])
        else:
            print(str(df[columns_list[i]]),
                  "is not a numerical column. Please use numerical column only.")