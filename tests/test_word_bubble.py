from PyDataPeek import word_bubble as bubble

import pandas.util.testing as tm
from pandas.util.testing import makeCustomDataframe as mkdf
import pytest
from wordcloud import WordCloud, STOPWORDS 
import matplotlib
import matplotlib.pyplot as plt 
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
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'E' : pd.Categorical(["test","train", np.NaN,"train"]),
                         'F' : 'foo' })
    
    fn = tmpdir_factory.mktemp('data')

    # Create different file types to test
    df.to_pickle(str(fn.join('df.pkl')))
    df.to_csv(str(fn.join('df.csv')))
    df.to_excel(str(fn.join('df.xls')))
    df.to_excel(str(fn.join('df.xlsx')))
    # bubble.word_bubble(str(make_files.join('df.pkl')))

    # Create and save image 
    bubble.word_bubble(file = str(fn.join('df.csv')), img_dir=str(fn), column="F")
    return fn

def test_csv_input(make_files):
    path_to_file = str(make_files.join('df.csv'))
    pd.testing.assert_frame_equal(bubble.read_file(path_to_file), pd.read_csv(path_to_file))
    

def test_excel_input(make_files):
    path_to_file = str(make_files.join('df.xls'))
    pd.testing.assert_frame_equal(bubble.read_file(path_to_file), pd.read_excel(path_to_file))
    # test another excel file format '.xlsx'
    pd.testing.assert_frame_equal(bubble.read_file(path_to_file + 'x'), pd.read_excel(path_to_file + 'x'))
    
def test_other_input(make_files):
    with pytest.raises(ValueError):
        bubble.word_bubble(str(make_files.join('df.pkl')))
        
def test_plot():
    df = pd.DataFrame({'F' : ['foo', 'blank', 'tom' ]})
    max_word = 50
    width = 800
    height = 800
    formated_words, stopwords = bubble.make_formated_words(df)              
    assert isinstance(bubble.make_cloud(formated_words, stopwords, max_word, width, height), matplotlib.figure.Figure)

def test_saved_file(make_files):
    assert os.path.isfile(str(make_files) + '0_wordcloud.png')