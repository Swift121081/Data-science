# Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

print(data.head())

# Set plot style
sns.set_style('whitegrid')

# Countplot for feature survived
sns.countplot(x='Gender', hue='Survived', data=data)

# Costomize plots
sns.countplot(x='Survived', data=data, palette='winter')

# Countplot for embarked
sns.countplot(x='Embarked', data=data)

# Rotate the value labels and modify their font size

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()

