# Step 0
import pandas as pd
import numpy as np
import xgboost
from sklearn import linear_model
from sklearn.preprocessing import OneHotEncoder

loc = '' # location if needed
train = pd.read_csv(loc+'train.csv')
test =  pd.read_csv(loc+'test.csv')

train_y = np.log(train['Sale_Price'])
train = train.drop(columns='Sale_Price')

# Step 1
def data_cleaning(X, quantile = None, category_model = None):
    data = X.copy()
    data = data.drop(columns=['PID','Street', 'Utilities', 'Condition_2', 'Roof_Matl', 'Heating', 'Pool_QC', 'Misc_Feature', 'Low_Qual_Fin_SF', 'Pool_Area', 'Longitude','Latitude'])

    data_num = data.select_dtypes('number')
    if quantile is None:
        quantile = data_num.quantile(0.95)
    data_num = data_num.clip(upper=quantile, axis=1)
    
    data_cat = data.select_dtypes(exclude='number')
    names_cat = data_cat.columns
    if category_model is None:
        category_model = OneHotEncoder(handle_unknown='ignore')
        category_model.fit(data_cat)
    data_cat = category_model.transform(data_cat).toarray()
    names_cat_proc = category_model.get_feature_names_out(names_cat)
    data_cat = pd.DataFrame(data_cat, columns = names_cat_proc)

    data = pd.concat([data_num, data_cat], axis=1).fillna(0)
    return data, quantile, category_model

train_proc, quantile, category_model = data_cleaning(train)

model1 = linear_model.RidgeCV() 
model1.fit(train_proc, train_y)

model2 = xgboost.XGBRegressor(n_estimators=5000, max_depth=6, eta=0.05, subsample=0.5, 
                              objective='reg:squarederror', seed = 0)
model2.fit(train_proc, train_y)

# Step 2
pid = test[['PID']].values.flatten()
test_proc, _, _ = data_cleaning(test, quantile, category_model)

y_pred1 = np.exp(model1.predict(test_proc).flatten())
y_pred2 = np.exp(model2.predict(test_proc).flatten())

pd.DataFrame({'PID':pid, 'Sale_Price': y_pred1}).to_csv(loc+'mysubmission1.txt',index=False)
pd.DataFrame({'PID':pid, 'Sale_Price': y_pred2}).to_csv(loc+'mysubmission2.txt',index=False)
