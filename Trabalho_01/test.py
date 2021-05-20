import pandas as pd
#import numpy as np

df = pd.read_excel('tabuas.xlsx')

dfc = df.columns

#contador para funções while
c = 0
#%%
#montando o df de at-2000
t = input('AT-2000 ou BR-EMSmt-v.2015? Selecione com A ou B\n')
if t.upper() == 'A':
    at = pd.DataFrame(df, columns = ['TÁBUA','AT-2000 FEMALE','AT-2000 MALE'])
    at.columns = ['IDADE', 'AT-2000-F', 'AT-2000-M']
    at.dropna(inplace=True)
    at = at.iloc[1:]
    tam = len(at['IDADE'])
    while True:
        g = input("Selecione o gênero com F ou M?\n")
 
        if g.upper() == 'F':
            s = 'AT-2000-F'
            break

        elif g.upper()== 'M':
            s = 'AT-2000-M'
            break
        else:
            print('Tente selecionar F ou M')
            
elif t.upper() == 'B':  
    at = pd.DataFrame(df, columns = ['TÁBUA','BR-EMSmt-v.2015-f','BR-EMSmt-v.2015-m'])
    at.columns = ['IDADE', 'BR-EMSmt-v.2015-F', 'BR-EMSmt-v.2015-M']
    at.dropna(inplace=True)
    at = at.iloc[1:]
    at = at[:-1]
    tam = len(at['IDADE'])
    while True:
        g = input("Selecione o gênero com F ou M?\n")
 
        if g.upper() == 'F':
            s = 'BR-EMSmt-v.2015-F'
            break

        elif g.upper()== 'M':
            s = 'BR-EMSmt-v.2015-M'
            break
        else:
            print('Tente selecionar F ou M') 
# %%
#Selecionar a taxa de juros
while True:      
    i = input('Qual a taxa de juros? Responda com 0.01 para 1% ao ano\n')
    try:
        j = float(i)
        break
    except ValueError:
        print('Tente colocar um número')
#%%
#Selecionar a população inicial
while True:      
    l = input('Qual a população inicial?\n')
    try:
        l0 = float(l)
        break
    except ValueError:
        print('Tente colocar um número')

#lista de colunas para adicionar ao dataframe
col_list = ['lx', 'dx','v^x','Dx','Nx','Cx','Mx']

#%%
#adiocionando todas as colunas ao dataframe
for i in col_list:
    at[i]= 0
    
#atribuindo o valor de l0 para a primeira coluna de lx 
at['lx'].iloc[0] = l0
#%%
#preencher os valores em lx e dx
tam_2 = tam - 1
while c < tam:
    at['dx'] = at['lx'] * at[s]
    lx_2 =  at['lx'] - at['dx']
    lx_2 = lx_2.iloc[0:tam_2]
    at['lx'].iloc[1:] = lx_2
    c +=1

#%%

#preencher os valores em v^x
at['v^x'] = 1/((1+j)**at['IDADE'])

#%%
#preencher os valores em Dx e Nx
at['Dx'] = at['lx'] * at['v^x']

at['Nx'].iloc[0] = at['Dx'].sum()
c = 1
while c < tam:
    at['Nx'].iloc[c] = at['Dx'].iloc[c:tam].sum()
    c +=1
    
# %%
#preencher os valores em Cx e Mx
at['Cx'] = at['dx'] * at['v^x']


at['Mx'].iloc[0] = at['Cx'].sum()
c = 1
while c < tam:
    at['Mx'].iloc[c] = at['Cx'].iloc[c:tam].sum()
    c +=1
    
