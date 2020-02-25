## PyDataPeek 

![](https://github.com/mirohu/pydatapeek/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/mirohu/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/mirohu/pydatapeek) ![Release](https://github.com/mirohu/pydatapeek/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pydatapeek/badge/?version=latest)](https://pydatapeek.readthedocs.io/en/latest/?badge=latest)

### Project Proposal
As data scientists, we are expected to orient business users to the datasets we are analyzing in a way that is accessible and easy to understand. This process is the first step to building trust in the analysis.

PyDataPeek is a package that enables data scientists to efficiently generate a visual summary of a dataset. This package includes functions that show the size of the dataset, a visual summary of missing data, a sample of the dataset showing the data types as well as exploratory visualizations for quantitative and qualitative data.

This package is also useful for business users who have to interact with data and want to begin exploring the data without using too much code or having to open a potentially large dataset on Excel. 

### Functions in this package
All functions take in csv or Excel files as inputs to generate user-friendly summaries of the ingested dataset.
1. **missing_data_overview**: Returns a visualization of the data where missing values are highlighted and the number of rows and columns are visually displayed.
2. **sample_data**: Returns a dataframe that displays the column names as rows, an example of one row, the data type of each column and summary statistics for each column depending on the data type. Quantitative measures will be summarized with a range, categorical values (i.e., less than 20 unique values) will be summarized by displaying the unique values, long form text data will be summarized with the average length of the response. 
3. **explore_with_histograms**: Returns histograms that shows the distribution of responses for given column(s). 
4. **explore_with_word_bubble**: Returns a word bubble visualization for text data given column name.

### How this fits in the Python ecosystem
(Instructions: are there any other Python or R software packages that have the same/similar functionality? Provide links to any that do. If none exist, then clearly state this as well)
- [Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/): ...
- [Python Pandas](https://pandas.pydata.org): Specifically, [`pd.describe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)
- [Python Altair](https://altair-viz.github.io): ...
- [Python Seaborn](https://seaborn.pydata.org): ...
- [Python WordCloud](https://github.com/amueller/word_cloud): ...


### Installation:
This project is under development! Upon it's first release, it can be installed with the following instructions.

```
pip install -i https://test.pypi.org/simple/ PyDataPeek
```

### Documentation
The official documentation is hosted on Read the Docs: <https://PyDataPeek.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).






