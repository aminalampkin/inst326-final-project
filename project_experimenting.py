# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:59:56 2019

@author: Graeme
"""

import csv
import pandas as pd
import seaborn as sea

raw = pd.read_csv('athlete_events.csv')

olympics = raw.drop(columns = ['Games', 'City', 'NOC', 'ID', 'Season', 'Name', 'Sex', 'Sport', 'Event', 'Medal'])

olympics['Height'] = olympics['Height']/100

olympics['BMI'] = olympics['Weight']/olympics['Height']

olympics = olympics[olympics.Year == 2008]

# Create an object for just the German Olympians
Germany = olympics[olympics.Team == 'Germany']

# Create an object for just the Chinese Olympians
China = olympics[olympics.Team == 'China']

China.isnull().sum()
Germany.isnull().sum()
olympics.isnull().sum()

olympics = olympics.dropna()

China = China.dropna()

Germany = Germany.dropna()

China.describe()

Germany.describe()

# Scatterplot
# Create scatterplot of the height and weight for both countries
sea.jointplot(x = 'Height', y = 'Weight', data = Germany)
sea.jointplot(x = 'Height', y  = 'Weight', data = China)

# Histogram
# Create a histogram of the height and weight for both countries
sea.distplot(China['Height'])
sea.distplot(China['Weight'])

sea.distplot(Germany['Height'])
sea.distplot(Germany['Weight'])

# Import Statsmodel library for regression
import statsmodels.formula.api as smf

# Create a fitted model for China
cLm = smf.ols(formula='Age ~ BMI', data=China).fit()

# Print the model summary for China
print(cLm.summary())

# Create a fitted model for Germany
gLm = smf.ols(formula='Age ~ BMI', data=Germany).fit()

# Print the model summary for the Germany
print(gLm.summary())

# Use the previously imported seaborn library to create another linear regression
# for China
sea.regplot(y = 'BMI', x = 'Age', data = China)

# Use the previously imported seaborn library to create another linear regression
# for Germany
sea.regplot(y = 'BMI', x = 'Age', data = Germany)

# Import stats from the scipy package
from scipy import stats

# Run a sample t-test
cTtest = olympics[olympics['Team']== 'China']['BMI']
gTtest = olympics[olympics['Team'] == 'Germany']['BMI']
stats.ttest_ind(cTtest, gTtest)   

