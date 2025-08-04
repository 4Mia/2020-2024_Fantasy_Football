# Package Upload
import pandas as pd # data manipulation
import streamlit as st # create web applications
import matplotlib.pyplot as plt # create visualizations
import glob # find pathnames matching a specifed pattern
import os # to interact with os

# Get all Excel files in current dir, read yr, add yr column & value,& combine into a single DF
file_paths = glob.glob('*.xlsx')
all_data = [] # List to hold combined excel files
for file in file_paths:
    # Extract year from filename for column labeling (assuming integer year in filename)
    filename = os.path.basename(file)
    year = ''.join(filter(str.isdigit,filename)) 
    df = pd.read_excel(file, header=1,engine='openpyxl')
    df['Year'] = year
    all_data.append(df) # Append each dataframe to the list
df = pd.concat(all_data, ignore_index=True) # Combine all dataframes into one

# Post DataFrame Evaluation and Cleanup
print(df.shape) # Display the dimensions combined dataframe to confirm successful loading
## print (df.head()) # Display the first few rows of the combined dataframe to review formatting
## print(df.describe()) # Display summary statistics of the combined dataframe to understand the data distribution
## print(df.info()) # Display information about the combined dataframe to check data types and non-null counts
df = df.drop(df.columns[27:32], axis=1) # Drop columns by index position (27 to 31, inclusive) not needed
df = df.fillna(0) # Convert all null (NaN) values in the DataFrame to 0
