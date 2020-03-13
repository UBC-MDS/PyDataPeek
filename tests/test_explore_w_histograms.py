from PyDataPeek import PyDataPeek as pdp
from PyDataPeek import explore_w_histograms as histograms
import pandas as pd
import numpy as np
import pytest
import os


@pytest.fixture(scope="session")
# makes a temperary file for testing
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
    pdp.explore_w_histograms(str(fn.join('df.csv')), columns_list=['C'])
    pdp.explore_w_histograms(str(fn.join('df.csv')), columns_list=['E'])
    return fn

# tests the read_file() for .csv input


def test_csv_input(make_files):
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(histograms._read_file(
        path_to_file), pd.read_csv(path_to_file))

# tests the read_file() for .xls and .xlsx input


def test_excel_input(make_files):
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(histograms._read_file(
        path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(histograms._read_file(
        path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))

# tests the explore_w_histograms() for other input to see if it raises errors


def test_other_input(make_files):
    with pytest.raises(ValueError):
        pdp.explore_w_histograms(str(make_files.join('df.pkl')), ['C'])

# test to see if the plots are saved


def test_saved_plot(make_files):
    assert os.path.isfile('C_chart.png')
    os.remove('C_chart.png')

# tests is_numeric() to see if it identifies numerical columns correctly


def test_non_numeric_column(make_files):
    path_to_file = str(make_files.join('df.csv'))
    df = pd.read_csv(path_to_file)
    assert histograms._is_numeric(df, 'C')
    assert not histograms._is_numeric(df, 'E')
    assert not os.path.isfile('E_chart.png')
