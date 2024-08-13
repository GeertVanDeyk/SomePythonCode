# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:32:03 2018

@author: gvandeyk

Script showing how to retrieve data from a URL
"""
import pandas as pd                       # PANDAS is used for DataAnalysis
import urllib                             # URLLIB gives access to URLs

# Defining output
MyOutputFile = '''C:/Users/gvandeyk/OneDrive - DXC Production/0 - ANALYSIS/'''
MyOutputFile = MyOutputFile + '''000_Python/MyOutput.csv'''

# Defining input = URL to capture data from
# (e.g. a CSV on public toilets in Antwerp)
MyURL = '''http://portaal-stadantwerpen.opendata.arcgis.com/datasets/'''
MyURL = MyURL + '''d5e587b30a9845e1814f4a1162668bae_8.csv'''

# Create a URL request
MyRequest = urllib.request.Request(MyURL)

# Open the URL request = launch the request
TheResponse = urllib.request.urlopen(MyRequest)

# Read the data
TheData_fromURL = pd.read_csv(TheResponse, sep=',')

# Prepare the data for output = create pandas dataframe
MyDataFrame = pd.DataFrame(TheData_fromURL.sort_values(
        ['POSTCODE', 'STADSEIGENDOM'], 0))

# Output the data to csv
MyDataFrame.to_csv(MyOutputFile)
