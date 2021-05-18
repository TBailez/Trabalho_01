import pandas as pd

df = pd.read_excel('tabuas.xlsx')

dfc = df.columns
at = pd.DataFrame(df, columns = ['TÁBUA','AT-2000 FEMALE','AT-2000 MALE'])
breme15 = pd.DataFrame(df, columns = ['TÁBUA','BR-EMSmt-v.2015-f','BR-EMSmt-v.2015-m'])
at.dropna(inplace=True) 
breme15.dropna(inplace=True)