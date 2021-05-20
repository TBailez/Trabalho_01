import pandas as pd
#import numpy as np

df = pd.read_excel('tabuas.xlsx')

dfc = df.columns

#taxa de juros
j = 0.01

#contador para funções while
c = 0

#população inicial
l0 = 10000000

#lista de colunas para adicionar ao dataframe
col_list = ['lx', 'dx','v^x','Dx','Nx','Cx','Mx']

#montando o df de at-2000
at = pd.DataFrame(df, columns = ['TÁBUA','AT-2000 FEMALE','AT-2000 MALE'])
at.columns = ['IDADE', 'AT-2000-F', 'AT-2000-M']
at.dropna(inplace=True)
at = at.iloc[1:]
#%%
#adiocionando todas as colunas ao dataframe
for i in col_list:
    at[i]= 0
    
#atribuindo o valor de l0 para a primeira coluna de lx 
at['lx'].iloc[0] = l0

#preencher os valores em lx e dx
while c < 116:
    at['dx'] = at['lx'] * at['AT-2000-F']
    lx_2 =  at['lx'] - at['dx']
    lx_2 = lx_2.iloc[0:115]
    at['lx'].iloc[1:] = lx_2
    c +=1

#%%
#preencher os valores em v^x
at['v^x'] = 1/((1+j)**at['IDADE'])

#preencher os valores em Dx e Nx
at['Dx'] = at['lx'] * at['v^x']

at['Nx'].iloc[0] = at['Dx'].sum()
c = 1
while c < 116:
    at['Nx'].iloc[c] = at['Dx'].iloc[c:116].sum()
    c +=1
# %%
#preencher os valores em Cx e Mx
at['Cx'] = at['dx'] * at['v^x']


at['Mx'].iloc[0] = at['Cx'].sum()
c = 1
while c < 116:
    at['Mx'].iloc[c] = at['Cx'].iloc[c:116].sum()
    c +=1
    
    
#%%
brems15 = pd.DataFrame(df, columns = ['TÁBUA','BR-EMSmt-v.2015-f','BR-EMSmt-v.2015-m'])
brems15.columns = ['IDADE', 'BR-EMSmt-v.2015-F', 'BR-EMSmt-v.2015-M']
brems15.dropna(inplace=True)
brems15 = brems15.iloc[1:]