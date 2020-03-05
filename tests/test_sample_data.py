from PyDataPeek import sample_data as sample

import pytest
import pandas as pd
import numpy as np
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
    sample.sample_data(str(fn.join('df.csv')))
    sample.sample_data(str(fn.join('df.csv')), sheet_name='abc')
    return fn

def test_csv_input(make_files):
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(sample.read_file(path_to_file), pd.read_csv(path_to_file))

def test_excel_input(make_files):
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(sample.read_file(path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    pd.testing.assert_frame_equal(sample.read_file(path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))

def test_other_input(make_files):
    with pytest.raises(ValueError):
        sample.sample_data(str(make_files.join('df.pkl')))

## test sample.summarize_data with sample dataframe