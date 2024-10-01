import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from ml.model import train_model, inference, compute_model_metrics
from ml.model import train_model 
import os

project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
data = pd.read_csv(data_path) # your code here


# TODO: implement the first test. Change the function name and input as needed
def test_inference():         #test inference data function
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path) # your code here
    X_train = data[["education-num", "age"]]
    y_train = data["salary"]
    model = train_model(X_train, y_train)
    y_pred = inference(model, X_train)
    
     # Check predictions
    assert isinstance(y_pred, np.ndarray), "Predictions are not returned as a NumPy array."
    assert len(y_pred) == len(X_train), "Number of predictions does not match the number of test samples."

# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():    #function to check performance of compute_model_metrics
    #X_train, y_train = data
    """project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path) # your code here
    X_train = data[["education-num", "age"]]
    y_train = data["salary"]"""
    X_train = np.random.rand(1000, 15)
    y_train = np.random.randint(2, size=1000)
    model = train_model(X_train, y_train) 
    #y_pred = inference(model, X_train)
    y_pred = model.predict(X_train)
    print(y_pred) 
    precision, recall, fbeta = compute_model_metrics(y=y_train, preds=y_pred)
    
    # To check if metrics are within valid range
    """
    assert 0 <= precision <= 1, "Precision is out of valid range."
    assert 0 <= recall <= 1, "Recall is out of valid range."
    assert 0 <= fbeta <= 1, "F-beta score is out of valid range."
"""
# TODO: implement the third test. Change the function name and input as needed
#def test_train_model():
   # X_train = np.random.rand(1000, 15)
   # y_train = np.random.rand(1000, 1)
    #model = train_model(X_train, y_train)

    #assert isinstance(model, RandomForestClassifier)

def test_train_model():
    #X_train, y_train = data
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path) # your code here
    X_train = data[["education-num", "age"]]
    y_train = data["salary"]
    model = train_model(X_train, y_train)

    # Check that the model is an instance of the expected model type
    assert isinstance(model, RandomForestClassifier)  # Adjust this based on your model type

    # Make predictions on the training data
    #predictions = model.predict(X_train)

    # Check that predictions are in the expected categories
    #assert all(pred in ['<=50K', '>50K'] for pred in predictions), "Predictions are not in the expected categories"