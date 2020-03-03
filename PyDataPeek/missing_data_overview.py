import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def missing_data_overview(file, sheet_name=0, dir=''):
    """Return a heatmap showing the missing values in the file.
    
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
    .png file
        heatmap of missing values, as a .png file
    
    Example
    -------
    >>> missing_data_overview(customers.xlsx, sheet_name='2019', dir='report')
    """
    # Check filetype and read file if valid
    if file.endswith('.csv'):
        df = pd.read_csv(file)
        print("TEST")
    else:
        try:
            df = pd.read_excel(file, sheet_name=sheet_name)
        except:
            raise ValueError("Please use a valid csv or excel file.")
    
    # Create heatmap
    plt.figure(figsize=(40, 20));
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis');
    plt.ylabel("Row number", fontsize=20);
    plt.xlabel("Column name", fontsize=20);
    plt.title("Heatmap of missing values", fontsize=20);

    # Save and return image file
    p = plt.savefig(f"./{dir}/{sheet_name}_heatmap.png", orientation='landscape', optimize=True, pad_inches=2, bbox_inches='tight');
    return p
