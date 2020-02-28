import pandas as pd


def sample_data(file, sheet_name=0, dir=''):
     """Return a data table showing column names in rows, an example record, column data types and
        summary statistics for numerical, categorical and long-form text data
     
     Parameters
     ----------
     file : str
         the name of the file, including the filetype extension
     sheet_name : int, optional
         if passing an excel file, the name of the sheet to analyze, by default 0
     dir : str, optional
         the directory where the file should be saved, by default ''
     
     Returns
     -------
     .csv file
        data table showing data summary, as a .csv file
        data summary includes column names in rows, an example record, column data types and
        summary statistics for numerical (range), categorical (unique values) 
        and long-form text data (average length of string)

     
     Example
     -------
     >>> sample_data(customers.xlsx, sheet_name='2019', dir='report')
     """
     # Check filetype and read file if valid
     if file.endswith('.csv'):
         df = pd.read_csv(file)
     else:
         try:
             df = pd.read_excel(file, sheet_name=sheet_name)
         except:
             print("Please use a valid csv or excel file.")

     # Create dataframe of data summary

     # Save and return csv
     # csv = pd.DataFrame.to_csv(summary)
     # return csv