from PyDataPeek import missing_data_overview as missing

import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope="session")
def make_files(tmpdir_factory):
    df = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
    fn = tmpdir_factory.mktemp('data')
    df.to_pickle(str(fn.join('df.pkl')))
    df.to_csv(str(fn.join('df.csv')))
    df.to_excel(str(fn.join('df.xls')))
    df.to_excel(str(fn.join('df.xlsx')))
    # missing.missing_data_overview(str(make_files.join('df.pkl')))
    return fn
    #df.to_excel('df.xlsx')
    #df.to_excel('df.xls')
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

def test_excel_input(make_files):
    with pytest.raises(ValueError):
        missing.missing_data_overview(str(make_files.join('df.xls')), dir = str(make_files))
    with pytest.raises(ValueError):
        missing.missing_data_overview(str(make_files.join('df.xlsx')))

def test_other_input(make_files):
    with pytest.raises(ValueError):
        missing.missing_data_overview(str(make_files.join('df.pkl')))

#def test_other_input():
#    df = pd.DataFrame({ 'A' : 1.,
#                         'B' : pd.Timestamp('20130102'),
#                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                         'D' : np.array([3] * 4,dtype='int32'),
#                         'E' : pd.Categorical(["test","train","test","train"]),
#                         'F' : 'foo' })
#    df.to_pickle('df.pkl')
#    with pytest.raises(ValueError):
#        missing.missing_data_overview('./df.pkl') 
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
