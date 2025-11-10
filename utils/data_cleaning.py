import numpy as np
import pandas as pd

class DataCleaner:
    def __init__(self, data_path: str):
        df = pd.read_csv(data_path)
        self.data = df.copy()
        
    def clean(self):
        print("Data Cleaning")

        
        missing = self.data.isnull().sum()
        print("Missing values by column:\n", missing)

        duplicates = self.data.duplicated().sum()
        print(f"Number of duplicate rows: {duplicates}")
        if duplicates > 0:
            self.data = self.data.drop_duplicates()
            print("Dropped duplicates.")

        return self.data
