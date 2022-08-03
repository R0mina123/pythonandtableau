# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:52:19 2022

@author: Owner
"""

import pandas as pd 
 
# file_name = pd.read_csv('file.csv') ---- format of read_csv

Data = pd.read_csv('transaction.csv')

Data = pd.read_csv('transaction.csv' , sep=';')

#summary of data
Data.info()

#working with calculations

#defining variable

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumbersOfItemsPurchased = 6 

#Mathematical Operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumbersOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumbersOfItemsPurchased*CostPerItem 
SellingPricePerTransaction = NumbersOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTrasaction = Numberofitemspurchased*costpeitem
#Variable name  = dataframe['coumn_name']

CostPerItem = Data['CostPerItem']
NumberOfItemsPurchased = Data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#To add as a additional column in dataframe

Data['CostPerTransaction'] = Data['CostPerItem'] * Data['NumberOfItemsPurchased']

#Sales per transaction 

Data['SalesPerTransaction'] = Data['SellingPricePerItem'] * Data['NumberOfItemsPurchased']

# profit = sales - cost

Data['ProfitPerTransaction'] = Data['SalesPerTransaction'] - Data['CostPerTransaction']

# markup = (Sales - cost)/cost

Data['Markup'] = ( Data['SalesPerTransaction'] - Data['CostPerTransaction'] )/ Data['CostPerTransaction']


#Rounding Markup for decimal digits, how many digit number can be mentioned in the end

roundmarkup = round(Data['Markup'], 2)

#Combining data fields

my_date= 'Day'+'-'+'Month'+'-'+'Year'

#my_date = Data['Day']+'-'

#checking columns data type
print(Data['Day'].dtype)

#Change columns type

day = Data['Day'].astype(str)
year = Data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'

my_date = day+'-'+ Data['Month']+'-'+year

Data['date'] = my_date

#using iloc to view specifc columns/rows

Data.iloc[0] #views the row with index = 0 
Data.iloc[0:3] #first 3 rows
Data.iloc[-5:] #last 5 rows


#Using split to split the clientkeyword field
#new_var =column.str.split('sep' , expand= True)

split_col = Data['ClientKeywords'].str.split(',' , expand=True)

#creating new coloumn for the split columns in client keyword

Data['ClientAge'] = split_col[0]
Data['ClientType'] = split_col[1]
Data['LengthOfContract'] = split_col[2]

#To get rid of brackets using replace function

Data['ClientAge'] = Data['ClientAge'].str.replace('[' , '')
Data['LengthOfContract'] = Data['LengthOfContract'].str.replace(']' , '')

#Using the lower function to change item to lowercase

Data['ItemDescription'] = Data['ItemDescription'].str.lower()

#How to merge files

#Bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv' , sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

Data = pd.merge(Data, seasons, on = 'Month')

#dropping columns

# df = df.drop('columnname' , axis =1)

Data = Data.drop('ClientKeywords' , axis = 1)
Data = Data.drop('Day' , axis = 1)

Data = Data.drop(['Year', 'Month'], axis = 1)

#Export into csv

Data.to_csv('ValueInc_Cleaned.csv' , index = False)
















 























































































































