# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:09:23 2018

@author: Karan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_data = pd.read_csv('./datasets/train.csv')

Y = train_data.iloc[:,1].values
X = train_data.drop(['PassengerId','Survived','Name','Ticket','Fare','Cabin'],axis=1)


train_data[['Pclass','Survived']].groupby(['Pclass']).describe()
train_data[['Sex','Survived']].groupby(['Sex']).describe()
train_data[['Embarked','Survived']].groupby(['Embarked']).describe()
train_data['total_members'] = train_data['SibSp']+train_data['Parch']

train_data[['total_members','Survived']].groupby('total_members').describe()



total_males = train_data[(train_data['Sex']=='male')]
males_survived = train_data[ (train_data['Sex']=='male' ) & (train_data['Survived']==1) ]
males_dead = train_data[ (train_data['Sex']=='male') & (train_data['Survived']==0) ]
bin_width = 5 
plt.show()
males_graph = total_males['Age'].plot(kind='hist' , bins = np.arange( 0, max(total_males['Age'])+bin_width,bin_width) , edgecolor='black' , label='Total Males'  )
xticks = np.arange(0,81,5)
males_graph.set_xticks(xticks)

males_survived['Age'].plot(kind='hist',bins = np.arange( 0, max(total_males['Age'])+bin_width,bin_width) , edgecolor='black' , label='Males Survived',alpha=0.4)
males_dead['Age'].plot(kind='hist',bins = np.arange( 0, max(total_males['Age'])+bin_width,bin_width) , edgecolor='black' , label='Dead Males',alpha=0.4)
males_graph.legend()
plt.show()

all_survived = train_data[(train_data['Survived'])==1]
all_dead = train_data[(train_data['Survived'])==0]
full_graph = all_survived['Age'].plot(kind='hist' ,bins = np.arange(0,max(train_data['Age'])+bin_width,bin_width) , ec='black', label ='All Survived')
full_graph.set_xticks(np.arange(0,81,5))
all_dead['Age'].plot(kind='hist',bins = np.arange(0,max(train_data['Age'])+bin_width,bin_width) , ec='black', label ='All dead' ,alpha = 0.4)
full_graph.legend()

#all elder persons survived , infants have high survival rate
