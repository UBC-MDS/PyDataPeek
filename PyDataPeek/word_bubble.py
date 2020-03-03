from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

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
    """
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        try:
            df = pd.read_excel(file, sheet_name=sheet_name)
        except:
            raise ValueError("Please use a valid csv or excel file.")
    return df

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
    df = read_file(file=file, sheet_name=sheet_name)
            
    df = df[column]
    
    formated_words = ' '
    stopwords = set(STOPWORDS)
    
    words = str(df)
    tokens = words.split()
    
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    
    for words in tokens: 
        formated_words = formated_words + words + ' '
        
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(formated_words) 
  
    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show()