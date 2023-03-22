from sklearn.linear_model import LinearRegression
from datetime import datetime
import pandas as pd 
import numpy as np


class LinearRegressionBalanceStatistics:
    __data: pd.DataFrame

    def __init__(self, data: dict) -> None:
        self.__data = pd.DataFrame(data)
        self.__data['date'].apply(func = pd.to_datetime)
        self.__data['date'] = self.__data['date'].apply(self.__oordinal_modified_transform)       


    def get_prediction_by_date(self, date: datetime):
        model = LinearRegression().fit(X = np.array(self.__data['date']).reshape(-1, 1), y = self.__data['balance'])
        ordinal_date = datetime.toordinal(date)

        prediction = model.predict([[ordinal_date]])
        
        return prediction[0] 

    def set_data(self, data: dict):
        self.__data = pd.DataFrame(data)
        self.__data['date'].apply(func = pd.to_datetime)
        self.__data['date'] = self.__data['date'].apply(self.__oordinal_modified_transform)   

    def __oordinal_modified_transform(self, date: datetime):
        return datetime.toordinal(date) + (date.hour/24)+ (date.minute/1440) + (date.second/86400)