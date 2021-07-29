# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:36:38 2021

@author: Ita
"""

import pandas as pd
import time
import numpy as np
import csv

start_time = time.time()

dict_letters = [['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'],
                [0, 1, 2, 3, 4, 5, 6],
                ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si'],
                ['C','D','E','F','G','A','B']]

df = pd.read_csv(r"C:\Users\Ita\Documents\GitHub\SolReSol\Solresol Dictionary - Solresol Dictionary.csv")
df.columns = ['SolReSol','English','Comments']
df = df.iloc[4:]

#df = df.iloc[:100]

df['Letter_0'] = -1
df['Letter_1'] = -1
df['Letter_2'] = -1
df['Letter_3'] = -1
df['Letter_4'] = -1
print('running dictionary on ',df.shape)
for index, row in df.iterrows():
    a = row['SolReSol']
    if (type(a) == str):
        #print(a.find(" "), index)
        if (a.find(" ") == -1):
            #print(a)
            #first letter
            for i1 in dict_letters[1]:
                if (a[0:2] == dict_letters[2][i1]):
                    #print(df['Letter_0'][index])
                    df['Letter_0'][index] = dict_letters[3][i1]
                    #print(df['Letter_0'][index])
                    if (i1 == 4):
                        a = a[3:]                    
                    else:
                        a = a[2:]
                    break    
            for i2 in dict_letters[1]:
                if (a[0:2] == dict_letters[2][i2].lower()):
                    df['Letter_1'][index] = dict_letters[3][i2]
                    if (i2 == 4):
                        a = a[3:]                    
                    else:
                        a = a[2:]
                    break 
            for i3 in dict_letters[1]:
                if (a[0:2] == (dict_letters[2][i3]).lower()):
                    df['Letter_2'][index] = dict_letters[3][i3]
                    if (i3 == 4):
                        a = a[3:]                    
                    else:
                        a = a[2:]
                    break 
            #print(a[0:2])
            for i4 in dict_letters[1]:
                if (a[0:2] == (dict_letters[2][i4]).lower()):
                    df['Letter_3'][index] = dict_letters[3][i4]
                    if (i4 == 4):
                        a = a[3:]                    
                    else:
                        a = a[2:]
                    break 
            for i5 in dict_letters[1]:
                if (a[0:2] == (dict_letters[2][i5]).lower()):
                    df['Letter_4'][index] = dict_letters[3][i5]
                    if (i5 == 4):
                        a = a[3:]                    
                    else:
                        a = a[2:]
                    break 
   # print(row['SolReSol'],row['Letter_0'])
df = df[df['Letter_0'] != -1] 
df = df[df['English'].isna() == False] 

df#df['Letter_0'].head(3000)
print('done in ',(time.time() - start_time),' seconds')
df = df[['SolReSol','English','Letter_0','Letter_1','Letter_2','Letter_3','Letter_4']]

df.to_csv('dict_to.csv', index=False, header=True, quoting=csv.QUOTE_ALL, line_terminator='],\n[')
        #singles
#AND CANCEL SO L_2 == -1
one_letter = df[df['Letter_1'] == -1]
#doubles
two_letter = df[df['Letter_2'] == -1]
two_letter.to_csv('doubles.csv', index=False, header=True)
two_letter[['SolReSol','English','Letter_0','Letter_1','Letter_2','Letter_3','Letter_4']].to_numpy()
#triples
three_letter = df[df['Letter_2'] != -1]
three_letter = three_letter[three_letter['Letter_3'] != -1]


#print(df.shape)

