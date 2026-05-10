import pandas as pd
import numpy as np

df = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce Purchases')
# print df.to_csv('temo.csv')

print df.shape[1]

'''
other ways 
len(ecom.colums)
ecom.info()

'''
print df['Purchase Price'].mean()
print df['Purchase Price'].max()
print df['Purchase Price'].min()

print len(df[df['Language'] == 'en'])
print len(df[df['Job'] == 'Lawyer'])

print len(df[df['AM or PM'] == 'PM'])
print len(df[df['AM or PM'] == 'AM'])

# 5 most popular titles

print df['Job'].value_counts()[0:5]
print df[df['Lot'] == "90 WT"]['Purchase Price']
print df[df['Credit Card'] == 4926535242672853]['Email']
print  len(df[(df['CC Provider'] == 'American Express') & (df ['Purchase Price'] > 95)])
print len (df [df['CC Exp Date'].apply(lambda exp : exp[3:] == '25')])
print df['Email'].apply(lambda exp : exp.split('@')[1]).value_counts()[0:5]