from PyDataPeek import sample_data as sample

import pytest
import pandas as pd
import numpy as np
import os
from xlrd import XLRDError

# create dummy dataframe for use in following tests


def create_data():
    # Create dummy data for tests
    df = pd.DataFrame({'A': 1.,
                       'B': pd.Timestamp('20130102'),
                       'C': pd.Series(1, index=list(range(4)),
                                      dtype='float32'),
                       'D': np.array([3] * 4, dtype='int32'),
                       'E': pd.Categorical(["test", "train", np.NaN, "train"]),
                       'F': 'foo'})

    return df

# create temporary session that stores csv, xls and xlsx files for testing
@pytest.fixture(scope="session")
def make_files(tmpdir_factory):
    # create dataframe
    df = create_data()

    # Create temporary directory to store test data
    fn = tmpdir_factory.mktemp('data')

    # Create different file types to test
    df.to_pickle(str(fn.join('df.pkl')))
    df.to_csv(str(fn.join('df.csv')))
    df.to_excel(str(fn.join('df.xls')), sheet_name='abc')
    df.to_excel(str(fn.join('df.xlsx')), sheet_name='abc')

    # Create and save csv
    sample.sample_data(str(fn.join('df.csv')))
    sample.sample_data(str(fn.join('df.csv')), sheet_name='abc')
    return fn

# test that function reads csv


def test_csv_input(make_files):
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(sample.read_file(
        path_to_file), pd.read_csv(path_to_file))

# test that function reads xls and xlsx


def test_excel_input(make_files):
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(sample.read_file(
        path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    pd.testing.assert_frame_equal(sample.read_file(
        path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))

# test that other file types raise errors


def test_other_input(make_files):
    with pytest.raises(XLRDError):
        sample.sample_data(str(make_files.join('df.pkl')))

# check that sample record is correctly obtained from data


def test_sample_record():
    df = create_data()
    results = sample.summarize_data(df)
    assert df.iloc[1].equals(results['sample_record'])

# check that column names are correctly obtained from data


def test_column_names():
    df = create_data()
    results = sample.summarize_data(df)
    assert df.columns.equals(results.index)

# check that data types are accurately obtained from data


def test_data_type():
    df = create_data()
    results = sample.summarize_data(df)
    assert df.dtypes.equals(results['data_type'])

# test that float64 data types are summarized by median value


def test_summary_float64():
    df = create_data()
    results = sample.summarize_data(df)
    df_result = 'median value: ' + str(np.median(df['A']))
    test_result = results['summary'][0]
    assert df_result == test_result

# test that data types that aren't float, int or string do not create a summary


def test_summary_other():
    df = create_data()
    results = sample.summarize_data(df)
    test_result_datetime = results['summary'][1]
    test_result_category = results['summary'][4]
    assert test_result_datetime == 'No summary available'
    assert test_result_category == 'No summary available'

# test that float32 data types are summarized by median value


def test_summary_float32():
    df = create_data()
    results = sample.summarize_data(df)
    df_result = 'median value: ' + str(np.median(df['C']))
    test_result = results['summary'][2]
    assert df_result == test_result

# test that int32 data types are summarized by number of unique values


def test_summary_int32():
    df = create_data()
    results = sample.summarize_data(df)
    df_result = 'unique values: ' + str(df['D'].unique().size)
    test_result = results['summary'][3]
    assert df_result == test_result

# test that string data is summarized by average length of string


def test_summary_string():
    df = create_data()
    results = sample.summarize_data(df)
    df_result = "average length of string: " + \
        str(round(np.mean([len(str(i)) for i in df['F']]), 1))
    test_result = results['summary'][5]
    assert df_result == test_result

# test that csv output file is saved properly


def test_saved_file(make_files):
    assert os.path.isfile('results.csv')
    os.remove('results.csv')
