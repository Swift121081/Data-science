# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#IMport dataset
#data=sns.load_dataset("Titanic Dataset")
data = pd.read_csv('Titanic Dataset.csv')
# import dataset
 
print(data.head())

print(data.dtypes)

# Nominal categorical variables
nominal_cat = ['Nmae','Ticket','Cabin']

# Ordinal categorical variables
ordinal_cat = ['Embarked','Gender']

# Median value of feature dender and embarked

print(data['Gender'].value_counts())

gender_categories = ['Female','Male']

data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]

print(data['Embarked'].value_counts())

embarked_categories = ['S','C','Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)