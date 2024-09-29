# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model created by Jennifer Keane. It uses RandomForestClassifier which combines multiple decision trees to improve predictive performance and control overfitting. 

## Intended Use
Intended use is to develop a classification model on publicly available Census Bureau data and do predictions based on salary of greater than or less than/equal to 50,000.

## Training Data
The model will be trained using census data to monitor the model performance on various data slices and will be deployed using the FastAPI package.

## Evaluation Data
The data included the following parameters: age, workclass, fnlgt,	education, education-num, marital-status, occupation,	relationship, race,	sex, capital-gain, capital-loss, hours-per-week, native-country, salary

## Metrics
Model was evaluated using F1 score.  The value is 0.6863

## Ethical Considerations
We are using sex and race data in the model which may cause some descrimination issues.  Might consider removing from model in the future.

## Caveats and Recommendations
The F1 result was not optimal.  Possibly consider using different classifier or use hyperparameter tuning.
