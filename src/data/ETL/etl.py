#!/usr/bin/env python
from iexfinance import get_historical_data
from datetime import datetime
import matplotlib.pyplot as plt

class Etl:
    """
    Extraction, transformation and load class for preparing data for machine learning operations

    """

    def __init__(self, df):
        self.df = df

    def extract(self):
        """
        Extract function to extract data and create a table to be used within machine learning
        :return:
        """

        start = datetime(2017, 2, 9)
        end = datetime(2017, 5, 24)

        self.df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
        self.df.head()

        return self.df

    def transform(self):
        """

        :return:
        """
        return self.df

    def load(self):
        """

        :return:
        """
        print("hej")
