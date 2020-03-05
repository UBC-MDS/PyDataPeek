from PyDataPeek import explore_w_histograms as histograms
import pandas as pd 
import numpy as np
import altair as alt
from altair_saver import save
import pytest
import xlwt
import xlrd
from openpyxl.workbook import Workbook
import os

@pytest.fixture(scope="session")
def make_files(tmpdir_factory):
    # Create dummy data for tests
    df = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train", np.NaN,"train"]),
                         'F' : 'foo' })

    # Create temporary directory to store test data
    fn = tmpdir_factory.mktemp('data')
    
    # Create different file types to test
    df.to_pickle(str(fn.join('df.pkl')))
    df.to_csv(str(fn.join('df.csv')))
    df.to_excel(str(fn.join('df.xls')), sheet_name='abc')
    df.to_excel(str(fn.join('df.xlsx')), sheet_name='abc')

    # Create and save image 
    histograms.explore_w_histograms(str(fn.join('df.csv')), columns_list = ['C'])
    histograms.explore_w_histograms(str(fn.join('df.csv')), columns_list = ['E'])
    return fn

def test_csv_input(make_files):
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(histograms.read_file(path_to_file), pd.read_csv(path_to_file))
    
def test_excel_input(make_files):
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(histograms.read_file(path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(histograms.read_file(path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))
    
def test_other_input(make_files):
    with pytest.raises(ValueError):
        histograms.explore_w_histograms(str(make_files.join('df.pkl')), ['C'])
        

def test_saved_plot(make_files):
    path_to_file = str(make_files.join('df.csv'))
    df = pd.read_csv(path_to_file)
    assert os.path.isfile('C_chart.png')
    
def test_non_numeric_column(make_files):
    path_to_file = str(make_files.join('df.csv'))
    df = pd.read_csv(path_to_file)
    assert histograms.is_numeric(df, 'C') == True
    assert histograms.is_numeric(df, 'E') == False
    assert os.path.isfile('E_chart.png') == False