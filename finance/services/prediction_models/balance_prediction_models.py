from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from datetime import datetime
import pandas as pd 
import numpy as np


class LinearRegressionBalanceStatistics:
    __data: pd.DataFrame
    __model: LinearRegression

    def __init__(self, data: dict) -> None:
        self.set_data(data)
        self.__model = LinearRegression().fit(X = np.array(self.__data['date']).reshape(-1, 1), y = self.__data['balance'])       

    def get_prediction_tendency(self):
        return self.__model.predict(np.array(self.__data['date']).reshape(-1, 1))

    def get_prediction_by_date(self, date: datetime):
        return self.__model.predict([[datetime.toordinal(date)]])[0]

    def set_data(self, data: dict):
        self.__data = pd.DataFrame(data)
        self.__data['date'].apply(func = pd.to_datetime)
        self.__data['date'] = self.__data['date'].apply(self.__oordinal_modified_transform)   

    def get_score(self):
        y_true = np.array(self.__data['balance'])
        y_predict = self.get_prediction_tendency()

        return r2_score(y_true, y_predict)

    def __oordinal_modified_transform(self, date: datetime):
        return datetime.toordinal(date) + (date.hour/24)+ (date.minute/1440) + (date.second/86400)