import pandas as pd
#import numpy as np

df = pd.read_excel('tabuas.xlsx')

atf = pd.DataFrame(df, columns = ['AT-2000 FEMALE'])
atf = atf.iloc[1:]
atf.dropna(inplace=True)

list_atf = atf['AT-2000 FEMALE'].to_list()
[float(i) for i in list_atf]
print(list_atf)