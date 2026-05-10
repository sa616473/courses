import numpy as np
import pandas as pd

df = pd.read_csv('Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv')
# print df.head()
df.to_csv('test.csv', index = False)

print df.info()

# in order to get the average of one column grab the column and run mean
print df['BasePay'].mean()


print df['OvertimePay'].max()
print df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

print df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPay']

print df[df['TotalPay'] == df['TotalPay'].max()]['EmployeeName']

print df[df['TotalPay'] == df['TotalPay'].min()]['EmployeeName']

byyear = df.groupby('Year')['BasePay']
print byyear.mean()

print df['JobTitle'].nunique()
print df['JobTitle'].value_counts()[0:5]
print sum(df[df['Year'] == 2013]['JobTitle'].value_counts()== 1)
print len (df [df['JobTitle'].str.find("chief") >= 0])

def cheif_string(title):
	if 'chief' in title.lower().split():
		return True
	else:
		return False

print sum(df['JobTitle'].apply(lambda x: cheif_string(x)))

df['title_len'] = df['JobTitle'].apply(len)
print df[['TotalPayBenefits','title_len']].corr()