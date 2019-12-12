#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:51:37 2019
####################################
#             INST326              #
#            12/11/2019            #
#           Liz Hughley            #
#             114813442            #
#           Final Project          #
####################################
@author: liz
"""
#import Libraries
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

#Data Cleaning
os.chdir("/Users/liz/Downloads/120-years-of-olympic-history-athletes-and-results/")
olympic_data = pd.read_csv("athlete_events.csv")
olympic_data_1=olympic_data.drop(columns=['Games','NOC','City','ID','Sex','Name','Season','Event','Sport','Medal'])
olympic_data_1['BMI'] = olympic_data_1['Weight']/(olympic_data_1['Height']/100)
olympic_data_1=olympic_data_1.dropna()
olympic_data_2016=olympic_data_1[olympic_data_1['Year']==2016]
olympic_data_US_2016 = olympic_data_2016[olympic_data_2016.Team=='United States']
olympic_data_Germany_2016 = olympic_data_2016[olympic_data_2016.Team=='Germany']

#Summary Statistics
olympic_data_US_2016.describe()
olympic_data_Germany_2016.describe()

#Scatterplots
sns.jointplot(x = 'Height', y = 'Weight', data = olympic_data_US_2016)
sns.jointplot(x = 'Height', y  = 'Weight', data = olympic_data_Germany_2016)

#Histogram for Height
fig = plt.figure(figsize=(10,6))
sns.distplot(olympic_data_Germany_2016['Height'])
sns.distplot(olympic_data_US_2016['Height'])
fig.legend(labels=['Germany','US'])

#Histogram for Weight
fig = plt.figure(figsize=(10,6))
sns.distplot(olympic_data_Germany_2016['Weight'])
sns.distplot(olympic_data_US_2016['Weight'])
fig.legend(labels=['Germany','US'])

#Linear Regression
lm = smf.ols(formula='BMI ~ Age', data=olympic_data_2016).fit()
print(lm.summary())
lm.params

#T-Test
from scipy import stats
olympic_data_2016_US = olympic_data_2016[ olympic_data_2016['Team'] == 'United States']['BMI']
olympic_data_2016_Germany = olympic_data_2016[ olympic_data_2016['Team'] == 'Germany']['BMI']
stats.ttest_ind(olympic_data_2016_US, olympic_data_2016_Germany)
