from PyDataPeek import missing_data_overview as missing
from PyDataPeek import sample_data as sample
from PyDataPeek import explore_w_histograms as histo
from PyDataPeek import word_bubble as word
import os


def missing_data_overview(file, sheet_name=0, dir=''):
    """Return a heatmap showing the missing values in the file.

    The heatmap returned is the same size and shape as the input dataframe, with rows along the x-axis and columns along the y-axis. "Missing values" are anything represented as NaN values when the dataframe is read into Pandas, and therefore empty strings like " " will not be recognized as missing. The heatmap shows missing values in yellow, and non-missing values in purple.

    Parameters
    ----------
    file : str
        the name of the file, including the filetype extension
    sheet_name : int, optional
        if passing an excel file, the name of the sheet to analyze,
        by default 0
    dir : str, optional
        the directory where the file should be saved, by default ''

    Returns
    -------
    .png file
        heatmap of missing values, as a .png file

    Example
    -------
    >>> missing_data_overview("customers.xlsx", sheet_name='2019',
        dir='report')
    """
    df = missing._read_file(file, sheet_name=sheet_name)
    fig = missing._make_plot(df)
    fig.savefig(f"{dir}{sheet_name}_heatmap.png", orientation='landscape',
                optimize=True, pad_inches=2, bbox_inches='tight')
    return


def sample_data(file, sheet_name=0, dir=''):
    """Returns  data table showing column names in rows, an example record,
    column data types and summary statistics for numerical, text data from
    Excel or csv data

     Parameters
     ----------
     file : str
         the name of the file, including the filetype extension
     sheet_name : int, optional
         if passing an excel file, the name of the sheet to analyze, default 0
     dir : str, optional
        the directory where the file should be saved, by default ''

    Returns
    -------
    .csv file
        data table showing data summary, as a .csv file
        data summary includes column names in rows, an example record, column
        data types and summary statistics for integer, string and float data


    Example
    -------
    >>> sample_datacustomers.xlsx, sheet_name='2019')
    """

    df = sample._read_file(file, sheet_name)
    results = sample._summarize_data(df)
    results.to_csv(os.path.join(dir, 'results.csv'))
    return


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

    df = histo._read_file(file, sheet_name=0)

    try:
        columns_list[0]
    except IndexError:
        raise ValueError("Make sure column name is in your data!")

    for i in range(0, len(columns_list)):
        if histo._is_numeric(df, columns_list[i]) is True:
            histo._make_save_histogram(df, columns_list[i])
        else:
            print(str(df[columns_list[i]]),
                  "is not a numerical column.",
                  "Please use numerical column only.")


def word_bubble(file, sheet_name=0, img_dir='', column='',
                max_words=50, height=800, width=800):
    """Return an image of a word bubble of qualitative responses (text)
    from a column(s) from a spreadsheet.

     Parameters
     ----------
     file : str
         the name of the file, including the filetype extension
     sheet_name : int, optional
         if passing an excel file, the name of the sheet to analyze,
          default = 0
     img_dir : str, optional
         the directory where the file should be saved, by default ''
     column : string or vector
        the columns header that are to be included in the word bubble
     max_words : int
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
     word_bubble(file='imdb_sample', sheet_name=0, img_dir='word_bubble.png',
     column='review', max_words=50, height=800, width=800)
     """
    df = word._read_file(file=file, sheet_name=sheet_name)

    try:
        df = df[column]
    except ValueError:
        raise ValueError("Make sure column name is in your data!")

    formated_words, stopwords = word._make_formated_words(df)

    plt = word._make_cloud(formated_words, stopwords, max_words, width, height)
    p = plt.savefig(f"{img_dir}{sheet_name}_wordcloud.png",
                    orientation='landscape', optimize=True, pad_inches=2,
                    bbox_inches='tight')
    return p
