import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# TODO: implement the first test. Change the function name and input as needed
@pytest.fixture   
def data():
    # Sample DataFrame for testing
    return pd.DataFrame({
    'age': [16, 17, 18, 22, 20]  # Example ages
    })

def test_check_age_restriction(data):
    """
    Check that no one under the age of 16 is in the census data.
    """
    assert all(data['age'] >= 16), "There are individuals under the age of 16 in the census data."


# TODO: implement the second test. Change the function name and input as needed
def test_data_shape():
    """
    check for null values in data
    """
    #Your code here
    data = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })
    assert data.shape==data.dropna().shape


# TODO: implement the third test. Change the function name and input as needed

def check_model_algorithm(model, expected_algorithm):
    """
    Test to see if model uses correct algorithm, RandomForestClassifier.
    """
    model_class_name = model.__class__.__name__
    return model_class_name == expected_algorithm

def test_check_model_algorithm():
    """
    Test to see if model uses the correct algorithm, RandomForestClassifier.
    """
    model = RandomForestClassifier()  # Create an instance of the model
    expected_algorithm = 'RandomForestClassifier'
    assert check_model_algorithm(model, expected_algorithm) is True


