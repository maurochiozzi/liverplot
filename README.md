# Liverplot
A simple Python script for real-time data plot based on CoreyMSchafer tutorial.

Liverplot allows the real-time plot of all or selected columns of a CSV file.

# First Steps
(Optional) Create a virtualenv, by your preference, and jump to it.

Install all dependencies using the following command

> pip install requirements.txt

# Usage
In a Python enviroment, import liverplot.py, then run

> liverplot.begin(data_file, x_axis)

## Arguments
### Required
- file_name: name of the file containing the data, in CSV format. Example: 'data.csv'
- x_axis: name of the columns that has the values to be ploted in the x-axis

### Optional
- file_path: relative or absolute path if your file ins't in the same folder of Liverplot. Default=''
- select_columns: array of columns for a partial dataframe plot. Example: ['column_1', 'column_2']. Default=None
- fresh_rate: plot fresh rate, in milliseconds. This value should be in compliance with your CSV fresh rate. Default=100
- sample: will plot the last n values from the dataframe. As default, it'll plot all values. Default=-1
- figsize: tupple of the figure size (x, y). Default=(15,6)

## Data Mockup
CoreyMSchafer has also developed a script to generate random values to be saved into a CSV file, which can be used to perform a live test. Get it on his [repository](https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/09-LiveData/data_gen.py).
