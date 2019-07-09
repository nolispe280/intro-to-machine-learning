import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'input/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Use the command you learned to view summary statistics of the data. Then fill in variables to answer the following questions
home_data.describe()

# print the list of columns in the dataset to find the name of the prediction target
home_data.columns

y = home_data.SalePrice

# Create the list of features below
feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']

# select data corresponding to features in feature_names
X = home_data[feature_names]

# Review data
# print description or statistics from X
X.describe()

# print the top few lines
print(X.head)

#specify the model.
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)

predictions = iowa_model.predict(X)
print(predictions)
