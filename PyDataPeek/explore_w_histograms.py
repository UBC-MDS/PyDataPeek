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

def check_columns(df, columns_list):
    """
    Helper function used to take a dataframe, a list of numerical column names. 
    Return none if all the columns are numerical, raise a print messages if 
    one of the column is not numeric
    
    Parameters
    --------
    file:
        a csv file
    coloumns: 
        a list of numerical column names as strings
    
    
    Returns
    -------
    None or a print message
    """
    for c in range(0, len(columns_list)):
        
        # check if the column is numerical
        if str(df[columns_list[c]].dtypes) == 'int64' or str(df[columns_list[c]].dtypes) == 'float64':
            return None
        else:
            print(df[columns_list[c]], 'is not a numerical column.'"Please use numerical column only.")
          
    
def make_histograms(df, columns_list):
    """
    Helper function used to take a dataframe, a list of numerical column names 
    and returns a png file of histogram(s)
    
    Parameters
    --------
    file:
        a csv file
    coloumns: 
        a list of numerical column names as strings
    
    
    Returns
    -------
    .png file(s) of histogram(s)
    """     
    for c in range(0, len(columns_list)):
        # plot and save the chart with different name
        chart = alt.Chart(df).mark_bar().encode(
                    alt.X(columns_list[c]+':Q', bin = True),
                    alt.Y('count()')
                )

        chart.save(columns_list[c] + '_chart' + '.png')
        
def explore_w_histograms(file, columns_list, sheet_name =0):
    """
    take a csv file, a sheet name (default 0),
    a list of numerical column names 
    and returns a png file of histogram(s)
    
    Parameters
    --------
    file:
        a csv file
    coloumns: 
        a list of numerical column names as strings
    
    
    Returns
    -------
    .png file(s) of histogram(s)
    
    Example
    -------
    >>> explore_w_histograms(['volumn', 'date'])
    """
    df = read_file(file, sheet_name = 0)
    check_columns(df, columns_list)
    make_histograms(df, columns_list)
    