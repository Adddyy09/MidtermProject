import pandas as pd
import os

class DataCuration:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs", exist_ok=True)

    def create_correlation_dataset(self):
        df = self.data[['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction']]
        df.to_csv('outputs/Correlation.csv', index=False)
        return df

    def create_descriptive_dataset(self):
        df = self.data[['Department', 'JobRole', 'Gender', 'MaritalStatus', 'Attrition']]
        df.to_csv('outputs/Descriptive.csv', index=False)
        return df

    def create_predictive_dataset(self):
        df = self.data[['Age', 'BusinessTravel', 'JobLevel', 'MonthlyIncome', 'OverTime', 'Attrition']]
        df.to_csv('outputs/Predictive.csv', index=False)
        return df
