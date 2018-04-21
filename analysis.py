# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:09:23 2018

@author: Karan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('./datasets/train.csv')

Y = train_data.iloc[:,1].values
X = train_data.drop(['PassengerId','Survived','Name','Ticket','Fare','Cabin'],axis=1)


classes = pd.value_counts(train_data['Sex'])


males_survived = pd.value_counts((train_data['Sex']=='male') & (train_data['Survived']==1)) 
females_survived = pd.value_counts((train_data['Sex']=='female') & (train_data['Survived']==1))

male_passengers = {}

train_data[['Pclass','Survived']].groupby(['Pclass']).describe()
train_data[['Sex','Survived']].groupby(['Sex']).describe()
train_data['Survived','Embarked'].groupby(['Embarked']).describe()
