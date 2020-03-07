from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd


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

def make_formated_words(df):
    """Helper function used to make the column into a vector that can be 
    read into the cloudword function object.
    
    Checks if file type is a .csv or excel. If not, returns a ValueError.
    Parameters
    ----------
    df : pandas.Dataframe
        The column(s) of the dataframe 
    
    Returns
    -------
    formated_words: str
        formated str for that can be inputed into the Wordcloud function
    stop_words: set
        set of english stopwords to be removed from the Wordcloud
    """
    formated_words = ' '
    stopwords = set(STOPWORDS)
    
    try:
        words = str(df)
    except:
        raise ValueError("Column cannot be formated for processing, please try a different one")
    tokens = words.split()
    
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    
    for words in tokens: 
        formated_words = formated_words + words + ' '
        
    return formated_words, stopwords


def make_cloud(formated_words, stopwords, max_words, width, height):
    """Return an plt of a word bubble of qualitative responses (text) from a column(s) from a spreadsheet.

     Parameters
     ----------
     formated_words: str
        formated str for that can be inputed into the Wordcloud function
     stop_words: set
        set of english stopwords to be removed from the Wordcloud
     max_words : int
         max number of words in the word bubble, default = 50 words
     height : int
        the height of the outputted image, default = 8 inches
     width : int 
        the width of the outputted image, default = 8 inches


     Returns
     -------
     plt : matplotlib.pyplot.plt
        returns an image of a word bubble by specified width and height
        and includes max number of words.

     """
    #create wordcloud object
    wordcloud = WordCloud(width = width, height = height, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10,
                max_words=max_words).generate(formated_words)
    
  
    # plot the WordCloud image                        
    fig = plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    return fig

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd


def word_bubble(file, sheet_name=0, img_dir='', column='', max_words=50, height=800, width=800):
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
        the height of the outputted image, default = 800 pixels
     width : int 
        the width of the outputted image, default = 800 pixels


     Returns
     -------
     .png file
        returns an image of a word bubble by specified width and height
        and includes max number of words.

     Example
     -------
     >>> word_bubble(file='imdb_sample', sheet_name=0, img_dir='word_bubble.png', column='review', max_words=50, height=800, width=800)
     """
    df = read_file(file=file, sheet_name=sheet_name)
    
    try:
        df = df[column]
    except:
        raise ValueError("Make sure column name is in your data!") 
    
    formated_words, stopwords = make_formated_words(df)
    
    plt = make_cloud(formated_words, stopwords, max_words, width, height)
    p = plt.savefig(f"{img_dir}{sheet_name}_wordcloud.png", orientation='landscape', optimize=True, pad_inches=2, bbox_inches='tight');
    return p   
    