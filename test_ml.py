import pytest
# TODO: add necessary import
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def check_age_restriction(data):
    """
    #  Check that no one under the age of 16 is in the census data.
    """
    # Your code here
         
    return all(data['age'] >= 16)


# TODO: implement the second test. Change the function name and input as needed
def test_dtat_shape():
    """
    # check for null values in data
    """
    # Your code here
    assert data.shape==data.dropna().shape


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
