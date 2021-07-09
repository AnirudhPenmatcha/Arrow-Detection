import pandas as pd

df = pd.read_csv('updated_new_train.csv')

for i in df.index:
    if(df['filename'][i].endswith('.jpg') == 0):
        df['filename'][i] = df['filename'][i] + '.jpg'

df.to_csv('updated_new_train.csv', index = None)
