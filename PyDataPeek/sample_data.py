import pandas as pd
import numpy as np

def read_file(file, sheet_name=0):
     """Helper function used to read the file and return a pandas dataframe.

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

     Example
     -------
    >>> read_file(customers.xlsx, sheet_name='2019')
     """
     if file.endswith('.csv'):
         df = pd.read_csv(file)
     else:
         try:
             df = pd.read_excel(file, sheet_name=sheet_name)
         except:
             raise ValueError("Please use a valid csv or excel file.")
     return df


def summarize_data(df):
    """Helper function that returns  data table showing column names in rows, an example record, column data types
    and summary statistics for numerical, text data
    
    Parameters
    ----------
     df : pandas.DataFrame
         the dataframe object to analyze
     
    Returns
    -------
    .csv file
        data table showing data summary, as a .csv file
        data summary includes column names in rows, an example record, column data types and
        summary statistics for integer, string and float data

     
    Example
    -------
    >>> summarize_data(df)
    """
    ## add record sample
    results = pd.DataFrame({'sample_record': df.iloc[1]})

    ## add data types
    results['data_type'] = df.dtypes

    ## add summary statistics based on data type
    summary = []
    for index, row in results.iterrows():
        if row['data_type'] == 'int64':
            summary.append("unique values: " + str(df[index].unique().size))
        elif row['data_type'] == 'object':
            summary.append("average length of string: " + str(round(np.mean([len(str(i)) for i in df[index]]), 1)))
        elif row['data_type'] == 'float64':
            summary.append("median value: " + str(np.median(df[index])))
        else:
            summary.append("No summary available")      
    results['summary'] = summary


    # save and return csv
    csv = results.to_csv()
    return csv


def sample_data(file, sheet_name=0)::
    """Returns  data table showing column names in rows, an example record, column data types
    and summary statistics for numerical, text data from Excel or csv data
    
     Parameters
     ----------
     file : str
         the name of the file, including the filetype extension
     sheet_name : int, optional
         if passing an excel file, the name of the sheet to analyze, by default 0
     
    Returns
    -------
    .csv file
        data table showing data summary, as a .csv file
        data summary includes column names in rows, an example record, column data types and
        summary statistics for integer, string and float data

     
    Example
    -------
    >>> sample_datacustomers.xlsx, sheet_name='2019')
    """

    df = read_file(file, sheet_name)
    csv = summarize_data(df)
    return csv