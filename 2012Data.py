####################################
#             INST326              #
#            12/2/2019             #
#           Amina Lampkin          #
#             115359970            #
#           Final Project          #
####################################

# Change the working directory
import os
os.chdir('/Users/aminasymone/Documents/INST326/Final Project')

# Import the necessary libraries
import pandas as pd

# Read the csv file using the Pandas library
original = pd.read_csv('athlete_events.csv')


#################### Clean the CSV file ####################
'''
We will be dropping the following columns from the dataset:
    - "Games"
    - "NOC"
    - "City"
    - "ID"
    - "Name"
    - "Sex"
    - "Event"
    - "Sex"
    - "Sport"
    - "Season"
    - "Medal"
'''

# Drop the four columns
olympics = original.drop(columns = ['Games', 'City', 'NOC', 'ID', 'Sex', 'Name', 'Event', 'Sport', 'Medal'])
'''
Part of our analysis will be comparing the Body Mass Index (BMI) of the athletes.
To calculate the BMI for this dataset there are several steps:
    1. Convert the height column from CM to M by dividing by 100.
    2. Calculate the BMI by dividing the weight by the new height
'''

# Convert the height column
olympics['Height'] = olympics['Height']/100

# Create the BMI column and calculate the index
olympics['BMI'] = olympics['Weight']/olympics['Height']

# Subset the data
'''
Each person in the group will be subsetting the data according to the year they chose. 
This file will be subset to only include 2012 data. 
'''

olympics12 = olympics[olympics.Year == 2012]

# Create an object for just the United States Olympians
unitedStates = olympics12[olympics12.Team == 'United States']

# Create an object for just the South Korean Olympians
southKorea = olympics12[olympics12.Team == 'South Korea']

#################### Descriptive Statistics ####################

# Missing values
'''
As data scientists, it's important to take note of the missing values within your dataset.
Before dropping any missing or null values, we'd like to take note of them.

There are 168 missing heights.
There are 360 missing weights. 
There are 396 missing BMIs.
'''

# Use the isnull() and sum() methods to gather a count of the missing values in the subset data
olympics12.isnull().sum()

# Now that we know where the missing observations are, we can drop them
olympics12 = olympics12.dropna()

# Use the isnull() and sum() methods to gather a count of the missing values in the subset data
unitedStates.isnull().sum()

# Use the isnull() and sum() methods to gather a count of the missing values in the subset data
southKorea.isnull().sum()

# Need to drop the one set of missing height, weight, BMI
southKorea = southKorea.dropna(subset = ['Height', 'Weight', 'BMI'])

# Descripitve stats for the numerical variables 
'''
To view the descriptive statistics for the Summer 2012 Olympics, please see 
the presentation. 
'''
# Use the describe() method to retrieve summary stats for the 2012 Olympics
olympics12.describe()
olympics12['Weight'].agg('mean')
olympics12['Weight'].std()

# Use the describe() method to retrieve summary statistics for the United States subset
unitedStates.describe()

# Use the describe() method to retrieve summary statistics for the South Korea subset
southKorea.describe()

#################### Histograms, Scatterplots, and Boxplots ####################


# Import the seaborn package to create the histograms and scatterplots
import seaborn as sea

# Boxplot
# Create a boxplot of the height and weight for the 2012 Olympic subset
sea.boxplot(y = 'Height', data = olympics12)
sea.boxplot (y = 'Weight', data = olympics12)


# Scatterplot
# Create scatterplot of the height and weight for both countries
sea.jointplot(x = 'Height', y = 'Weight', data = unitedStates)
sea.jointplot(x = 'Height', y  = 'Weight', data = southKorea)


# Histogram
# Create a histogram of the height and weight for both countries
sea.distplot(unitedStates['Height'])
sea.distplot(unitedStates['Weight'])

sea.distplot(southKorea['Height'])
sea.distplot(southKorea['Weight'])

#################### Regression ####################

# Import Statsmodel library for the first regression
import statsmodels.formula.api as smf

# Create a fitted model for the Olympic games from 2004 - 2016
totalRegression = olympics[olympics.Season == 'Summer']
totalRegression = olympics[olympics.Year >= 2004]
totalRegression = totalRegression.dropna()
totalLM = smf.ols(formula = 'BMI ~ Age', data = totalRegression).fit()
# Print the model summary for the summer 2004 - 2016 Olympics
print(totalLM.summary())

# Create a fitted model for the United States
usLm = smf.ols(formula='BMI ~ Age', data=unitedStates).fit()
# Print the model summary for the United States
print(totalLM.summary())

# Create a fitted model for the South Korea
skLm = smf.ols(formula='BMI ~ Age', data=southKorea).fit()
# Print the model summary for the South Korea
print(skLm.summary())



# Use the previously imported seaborn library to create another linear regression
# for all the Olympics
sea.regplot(y = 'BMI', x = 'Age', data = totalRegression)

# Use the previously imported seaborn library to create another linear regression
# for the United States
sea.regplot(y = 'BMI', x = 'Age', data = unitedStates)

# Use the previously imported seaborn library to create another linear regression
# for South Korea
sea.regplot(y = 'BMI', x = 'Age', data = southKorea)
#################### T-Test ####################

# Comparison
'''
In 2012, the United States was the number one country for medal counts and South Korea
was in fifth place for the number of medals they had. For the two countries, we are
trying to determine if there is statistically significant difference between the 
BMI in each country.

Alpha = 0.05
T-test statistic = 1.2332232487335777
P-value = 0.21847423917858688
'''
# Import stats from the scipy package
from scipy import stats

# Run a sample t-test
usTtest = olympics[olympics['Team']== 'United States']['BMI']
skTtest = olympics[olympics['Team'] == 'South Korea']['BMI']
stats.ttest_ind(usTtest, skTtest)   

'''
Questions to ask:
    - descriptive stats for a categorical variable
    - showing two countries on one histogram
'''
