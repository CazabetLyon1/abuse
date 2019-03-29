import pandas as pd

keys = pd.read_csv('keys.csv', delimiter = ',')
print ('manged to import csv file with success \n')
key_reduced =  keys.drop_duplicates()
print ('droped duplicates \n')
key_reduced.to_csv('keys_reduced.csv' , index=False)
print ('export succeed as key_reduced.csv')

