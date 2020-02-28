""" 
Script used take a csv file path, a list of numerical column names 
    and returns a png file of histogram(s)

Usage:
  explore_w_histograms.py --file=<file_path> --columns=<column_names>
Example:
  python explore_w_histograms.py --file=toy_dataset.csv --columns=Age,Illness
"""
from docopt import docopt
import pandas as pd
import altair as alt
from altair_saver import save

opt = docopt(__doc__)


def main(file, column_names):
    """
    take a csv file, a string of numerical column names
    and returns a png file of histogram(s)
    
    Parameters
    --------
    file:
        a csv file path
    coloumn_names: 
        a string of numerical column names, seperate with comma
    
    
    Returns
    -------
    .png file(s) of histogram(s)
    
    Example
    -------
    >>> explore_w_histograms('toy_dataset.csv', "volumn,date"])
    """
    # Check filetype and read file if valid
    if file.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        try:
            df = pd.read_excel(file, sheet_name=sheet_name)
        except:
            print("Please use a valid csv or excel file.")
    columns = column_names.replace(',',' ').split()
    
    for c in range(0, len(columns)):
        
        # check if the column is numerical
        if str(df[columns[c]].dtypes) == 'int64' or str(df[columns[c]].dtypes) == 'float64':
            
            # plot and save the chart with different name
            chart = alt.Chart(df).mark_bar().encode(
                alt.X(columns[c]+':Q', bin = True),
                alt.Y('count()')
            )
        
            chart.save(columns[c] + '_chart' + '.png')
            
        else:
            print("Please use numerical column only")

# Change the input to a list of strings

if __name__ == "__main__":
    main(opt["--file"], opt["--columns"])