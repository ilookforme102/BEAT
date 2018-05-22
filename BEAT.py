# -*- coding: utf-8 -*-
"""
Created on Mon May 21 04:59:07 2018

@author: Lenovo
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
os.getcwd()

file = "BEAT.xlsx"
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('Sheet1')
df1.tail()
df1.info()
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ="NaN", strategy = "mean", axis = 0)
imputer.fit(df1.iloc[:,1:22].values)
df1.iloc[:,1:22] = imputer.transform(df1.iloc[:,1:22].values)
#visualization for the whole data table
df1.columns = ['Country', 'Percent Expend',
       'Expend PPP',
       'Gov and Insu Percent',
       'Gov and Insu PPP',
       'OUP Percent',
       'OUP PPP',
       'Pharma and Medic Percent',
       'Pharma and Medic PPP',
       'Physicia Density',
       'Doctors consultations',
       'Inpatient stays',
       'Consultations per Doctor',
       'Inpatient discharge',
       'Infant mortality',
       'Life lost females',
       'Life lost male',
       'Life lost',
       'Life Expectancy', 'breast cancer',
       'cervix cancer', 'Prevent Expend']
print(df1.columns.values)
x = df1["Doctors consultations"]
y = df1["Infant mortality"]
plt.scatter(x, y, alpha=0.5)
plt.title('Relation between number of doctor visits and infant mortality (per 1000 live birth)')
plt.xlabel('x')
plt.ylabel('y')
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.show()

x2 = df1['Life Expectancy']
y2 = df1['Percent Expend']
plt.scatter(x, y, alpha=0.5)
plt.title('Relation between LE and health expenditure %')
plt.xlabel('x')
plt.ylabel('y')
z = np.polyfit(x2, y2, 1)
p = np.poly1d(z)
plt.plot(x2,p(x2),"r--")
plt.show()

# pie chart for the umet needs
df2 = xl.parse('unmet')
import matplotlib.pyplot as plt
 
# Data to plot
labels = ''
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

 
# Plot
plt.pie(df2, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
# pie chart for the LE and expenditure on heath


x3 = df1['Life Expectancy']
y3 = df1['Expend PPP']
plt.scatter(x3, y3, alpha=0.5)
plt.title('Relation between LE and expenditure on health PPP')
plt.xlabel('x3')
plt.ylabel('y3')
z = np.polyfit(x3, y3, 1)
p = np.poly1d(z)
plt.plot(x3,p(x3),"r--")
plt.show()

