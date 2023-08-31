from dataframe import show_columns, check_nan
import pytest
import pandas as pd

@pytest.fixture
def create_dataframe():
    return pd.read_csv("raw/data.csv")

class TestClass:
    def test_show_columns(self, create_dataframe):
        cols = show_columns(df=create_dataframe)
        expected_cols = ['date', 'reg', 'name', 'prod', 'qty', 'price', 'total_price']
        assert cols.tolist() == expected_cols
    
    def test_check_nan(self, create_dataframe):
        has_nan = check_nan(df=create_dataframe, col="name")
        assert not has_nan