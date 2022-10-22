import pandas as pd 
import matplotlib as mp

df= pd.concat(pd.read_excel("UFC Roster Departures.xlsx", sheet_name=None),ignore_index=True)#Combines all the sheets into one dateframe

df.rename(columns = { 'Unnamed: 2':'Reason'}, inplace = True)#gives a name to unnamed column

df.drop(labels=[0],axis=0,inplace=True) #removes empty first row

df2=df.fillna("Reason N/a")# creates 2nd data frame with NaN cells as "Reason N/a"

'''
THE DATA FRAME HAS MISSING VALUES FROM COMBINIGNG THE SPREADSHEETS
df2['Date'] = pd.to_datetime(df2['Date']).dt.normalize()


print(df2)
'''