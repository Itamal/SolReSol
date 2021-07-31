# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:36:38 2021

@author: Ita
"""
from __future__ import unicode_literals

import pandas as pd
import time
import numpy as np
import csv
import glob
# coding: utf8

start_time = time.time()

dict_letters = [['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'],
                [0, 1, 2, 3, 4, 5, 6],
                ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si'],
                ['C','D','E','F','G','A','B']]

df = pd.read_csv(r"C:\Users\Ita\Documents\GitHub\SolReSol\SolReSol\Solresol Dictionary - Solresol Dictionary.csv")
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

dbF = pd.DataFrame()

for name in glob.glob("C:/Users/Ita/Documents/GitHub/SolReSol/SolReSol/kgarrett-emojis/*"):
    db = pd.read_csv(name)
    x = name.replace('C:/Users/Ita/Documents/GitHub/SolReSol/SolReSol/kgarrett-emojis\\', '')
    db['type'] = x.replace('.csv', '')
    db = db[db.columns[2:5]]
    dbF = pd.concat([dbF, db])
print(dbF)
dbF.dropna(inplace=True)

db = pd.read_csv("C:/Users/Ita/Documents/GitHub/SolReSol/SolReSol/dict_to.csv")
#db.dropna(inplace=True)
db['emojis'] = np.nan
db['emojicount'] = 0
db['emojistypes'] = np.nan
db = db.apply(lambda s: s.fillna({i: [] for i in db.index}))
for index, row in db.iterrows():
    a = (row[1].split(' ', 1)[0]).split(',', 1)[0]
    for indexDBF, rowDBF in dbF.iterrows():
        #print('RDY',a,rowDBF[1],rowDBF)
        if (rowDBF[1].find(a.lower()) > -1):
            #print('BINGO',rowDBF[0],row[0],row[1],rowDBF[1])
            db['emojis'][index].append(rowDBF[2])
            db['emojistypes'][index].append(rowDBF[0])
            db['emojicount'][index] = db['emojicount'][index] + 1
            if (db['emojicount'][index] > 5):
                break
    # option two - look emoji by emoji and find what fits it
    # for i in rowDBF -> a.lower().find(rowDBF[1])
    if (index%33 == 0):
        print(index)
        db.to_csv('emojis.csv', index=False, header=True, encoding='utf-8-sig', quoting=csv.QUOTE_ALL, line_terminator='],\n[')
db.to_string()
