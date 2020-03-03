from PyDataPeek import missing_data_overview as missing

import pandas.util.testing as tm
from pandas.util.testing import makeCustomDataframe as mkdf
import pytest
import pandas as pd
import numpy as np

#def test_csv_input():
#    df = pd.DataFrame({ 'A' : 1.,
#                         'B' : pd.Timestamp('20130102'),
#                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                         'D' : np.array([3] * 4,dtype='int32'),
#                         'E' : pd.Categorical(["test","train","test","train"]),
#                         'F' : 'foo' })
#    df_csv = df.to_csv('df.csv')
#
#def test_excel_input():
#    df = pd.DataFrame({ 'A' : 1.,
#                         'B' : pd.Timestamp('20130102'),
#                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                         'D' : np.array([3] * 4,dtype='int32'),
#                         'E' : pd.Categorical(["test","train","test","train"]),
#                         'F' : 'foo' })
#    df_excel = df.to_excel('df.xlsx', sheet_name='Sheet A')
#
#
def test_other_input():
    df = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
    df = mkdf(5, 3)
    #with tm.ensure_clean('my_file_path') as path:
    df.to_pickle('df.pkl')
    with pytest.raises(ValueError):
        missing.missing_data_overview('./df.pkl') 
#
#def test_plot():
## how to test if plot not returned
#
#def test_saved_file():
## saved in correct folder, with correct filename, correct filetype
#
#def test_sheet_name():
#
#def test_dir():
