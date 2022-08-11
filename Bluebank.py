# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:54:13 2022

@author: Owner
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
    
#transform to dataframe
loandata = pd.DataFrame(data)

#Finding unique values for the purpose column
loandata['purpose'].unique()

#how to describe the data
loandata.describe()

#describe the data for specific coloumn
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()


#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income

#working with arrays

#1D array
arr = np.array([1, 2, 3, 4])

#0D array
arr = np.array(43)



#working with if statements

a = 40
b = 100

if b > a:
    print('b is greater than a')

#Adding more conditions

a = 40
b = 100
c = 1000

if b > a and b < c:
    print('b is greater than a but lesser than c')
    
#when conditions are not met
a = 40
b = 100
c = 10

if b > a and b < c:
    print('b is greater than a but lesser than c')
else:
    print('no conditions met')
    
#another condition of different metrics
a = 40
b = 100
c = 50

if b > a and b < c:
    print('b is greater than a but lesser than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('no conditions met')
    
    
    
#using or 
a = 40
b = 100
c = 50

if b > a or b < c:
    print('b is greater than a or lesser than c')
else:
    print('no conditions met')
    
#FICO Score

fico = 250

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent' 

if fico >= 300 and fico <400:
    ficocat = 'Very Poor'
elif fico>= 400 and fico <600:
    ficocat = 'Poor'
elif fico>= 601 and fico <660:
    ficocat = 'Fair'
elif fico>= 660 and fico <700:
    ficocat = 'Good'
elif fico>= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#for loops

fruits = ('apple' , 'banana' , 'pear' , 'cherry')

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)


for x in range(0,4):
    y = fruits[x]
    print(y)

#applying for loops to loan data

#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >=400 and category < 600:
        cat = 'Poor'
    elif category >=601 and category < 660:
        cat = 'Fair'
    elif category >=660 and category < 700:
        cat = 'Good'
    elif category >=700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)
        
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


#while loops

i = 1

while i < 10:
    print(i)
    i = i + 1 
    


#df loc as conditional statements
# df.localdf[columnname] condtion, newcolumnname = 'value if the condtions is met'

#for interest rate, a new column is wanted. rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] < 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width =0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'yellow' , width = 0.1)
plt.show()

#scatter plots

ypoint = loandata['annual income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv' , index = True)




 
































 
    
 











   
        







































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




































































