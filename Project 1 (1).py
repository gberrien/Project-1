#!/usr/bin/env python
# coding: utf-8

# In[2]:


#imports
import json 
import requests
import urllib.request
import mysql.connector
import pandas as pd
import numpy as np
import builtins
from pathlib import Path

#Step 1: Extract
path_to_file = "exports and imports of india(1997-2022) - exports and imports.csv"
path = Path(path_to_file)
if path.is_file():
    print(f'The file {path_to_file} exists')
    file = pd.read_csv("/Users/graceberrien23/Desktop/exports and imports of india(1997-2022) - exports and imports.csv")
    
    #clean up data
    file = file.replace(',','', regex=True)
    file = file.replace('NaN','np.nan', regex=True)
    file = file.dropna()
    
    #Step 3: Transform
    file2 = file.drop("Total Trade",1)
    
    #Step 2&4: Load with User Input
    input_string = input('Enter "csv" or "json"')
    #print('file end: ', input_string)
    while input_string!= "csv" and input_string!= "json":
    #if input_string == "csv" or input_string == json:
        print("Invalid file end. Only csv or json. Enter file end again.")
        input_string = input('Enter "csv" or "json"')
    print(input_string)
    newCSVName = "/Users/graceberrien23/Desktop/Exports and Imports of India(1997-2022)."+str(input_string)
    newCSV = file2.to_csv("/Users/graceberrien23/Desktop/Exports and Imports of India(1997-2022)."+str(input_string))
    
    #Step 5: Summary
    newFile = pd.read_csv(newCSVName)
    numRecords = len(newFile)
    print("Number of records: " + str(numRecords))
    numColumns = len(newFile.columns)
    print("Number of columns: " + str(numColumns))
    
    countries = file2.Country.unique()
    try:
    
        df = pd.DataFrame()
     
        for country in countries:
            selectedCountry = file2[file2["Country"]==str(country)]
            myList = []
            for item in selectedCountry["Trade Balance"]:
                item = float(item)
                myList.append(item)
            sumPos = sum(x > 0 for x in myList)
            posPercent = round((sumPos/len(selectedCountry))*100, 2)
            sumNeg = sum(x < 0 for x in myList)
            negPercent = round((sumNeg/len(selectedCountry))*100, 2)
            #print(str(country) + " has " + str(posPercent) + "% of years with a positive trade balance and " + str(negPercent) + "% of years with a negative trade balance.")   
            data = pd.DataFrame({"Country": [country], 'Percent Positive Trade Balance': [posPercent], 'Percent Negative Trade Balance': [negPercent]})
            df = df.append(data)
        pd.set_option('display.max_rows', None)
        print(df)
            
    except:
        print("There's an error")
            
else:
    print(f'The file {path_to_file} does not exist')


# In[ ]:




