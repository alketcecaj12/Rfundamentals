import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
from statsmodels.tsa.vector_ar.var_model import VAR
warnings.filterwarnings('ignore')


def data_preprocess(data): 
    """This function will take care of filling missing data and dropping non relevant columns. It takes as input the main dataframe"""
    new_cols = []
    for i in data.columns: 
        if i.startswith("latest_forecasted_"):
            new_cols.append(i)

    new_cols.append("carbon_intensity_avg")

    new_data = data[new_cols]
    
    for i in new_data.columns: 
         new_data[i] = new_data[i].bfill().ffill()

    new_data.drop("latest_forecasted_power_net_import_SE_avg", axis = 1, inplace = True)
    X = new_data.values
    
    return X


def deliver_forecasting(X, steps_ahead): 
    """This function will deliver the forecast. It takes as input the main data and the steps to forecast ahead"""
    model = VAR(X)
    model_fit = model.fit()
        
    yhat = model_fit.forecast(model_fit.endog, steps= steps_ahead)

    forecasted_y = yhat[:, -1]
    
    return forecasted_y

    
    