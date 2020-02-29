import pandas as pd

def sample_data(file, sheet_name=0, dir='', column='', max=50, height=8, width=8):
     """Return an image of a word bubble of qualitative responses (text) from a column(s) from a spreadsheet.
        
     
     Parameters
     ----------
     file : str
         the name of the file, including the filetype extension
     sheet_name : int, optional
         if passing an excel file, the name of the sheet to analyze, default = 0 
     dir : str, optional
         the directory where the file should be saved, by default ''
     column : string or vector
        the columns header that are to be included in the word bubble
     max : int
         max number of words in the word bubble, default = 50 words
     height : int
        the height of the outputted image, default = 8 inches
     width : int 
        the width of the outputted image, default = 8 inches
    
     
     Returns
     -------
     .png file
        returns an image of a word bubble by specified width and height
        and includes max number of words.
     
     Example
     -------
     >>> sample_data(customers.xlsx, sheet_name='2019', dir='report', column='review', max=50, height=7, width=7)
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