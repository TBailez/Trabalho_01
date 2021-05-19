import pandas as pd

df = pd.read_excel('tabuas.xlsx')

dfc = df.columns
at = pd.DataFrame(df, columns = ['TÁBUA','AT-2000 FEMALE','AT-2000 MALE'])
brems15 = pd.DataFrame(df, columns = ['TÁBUA','BR-EMSmt-v.2015-f','BR-EMSmt-v.2015-m'])
at.columns = ['IDADE', 'AT-2000-F', 'AT-2000-M']
brems15.columns = ['IDADE', 'BR-EMSmt-v.2015-F', 'BR-EMSmt-v.2015-M']
at.dropna(inplace=True) 
brems15.dropna(inplace=True)