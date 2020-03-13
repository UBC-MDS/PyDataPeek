from PyDataPeek import PyDataPeek as pdp
from PyDataPeek import missing_data_overview as missing

import pytest
import pandas as pd
import numpy as np
import matplotlib
import os


@pytest.fixture(scope="session")
def make_files(tmpdir_factory):
    # Create dummy data for tests
    df = pd.DataFrame(
        {'A': 1.,
         'B': pd.Timestamp('20130102'),
         'C': pd.Series(1, index=list(range(4)), dtype='float32'),
         'D': np.array([3] * 4, dtype='int32'),
         'E': pd.Categorical(["test", "train", np.NaN, "train"]),
         'F': 'foo'})

    # Create temporary directory to store test data
    fn = tmpdir_factory.mktemp('data')

    # Create different file types to test
    df.to_pickle(str(fn.join('df.pkl')))
    df.to_csv(str(fn.join('df.csv')))
    df.to_excel(str(fn.join('df.xls')), sheet_name='abc')
    df.to_excel(str(fn.join('df.xlsx')), sheet_name='abc')

    # Create and save image
    pdp.missing_data_overview(str(fn.join('df.csv')), dir=str(fn))
    pdp.missing_data_overview(
        str(fn.join('df.csv')), dir=str(fn), sheet_name='abc')
    return fn


def test_csv_input(make_files):
    # tests the read_file() for .csv input
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(missing._read_file(
        path_to_file), pd.read_csv(path_to_file))


def test_excel_input(make_files):
    # tests the read_file() for .xls and .xlsx input
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(missing._read_file(
        path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    pd.testing.assert_frame_equal(missing._read_file(
        path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))


def test_other_input(make_files):
    # tests for error if file is not a csv or excel
    with pytest.raises(ValueError):
        pdp.missing_data_overview(str(make_files.join('df.pkl')))


def test_plot(make_files):
    # tests that plot is created
    path_to_file = str(make_files.join('df.csv'))
    df = pd.read_csv(path_to_file)
    assert isinstance(missing._make_plot(df), matplotlib.figure.Figure)


def test_saved_file(make_files):
    # tests that plot file is saved
    assert os.path.isfile(str(make_files) + '0_heatmap.png')


def test_saved_file_withdir(make_files):
    # tests that plot file is saved if dir is passed
    assert os.path.isfile(str(make_files) + 'abc_heatmap.png')
