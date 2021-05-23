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
    dataset = pd.DataFrame(df, columns = ['TÁBUA','AT-2000 FEMALE','AT-2000 MALE'])
    dataset.columns = ['IDADE', 'AT-2000-F', 'AT-2000-M']
    dataset.dropna(inplace=True)
    dataset = dataset.iloc[1:]
    tam = len(dataset['IDADE'])
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
    dataset = pd.DataFrame(df, columns = ['TÁBUA','BR-EMSmt-v.2015-f','BR-EMSmt-v.2015-m'])
    dataset.columns = ['IDADE', 'BR-EMSmt-v.2015-F', 'BR-EMSmt-v.2015-M']
    dataset.dropna(inplace=True)
    dataset = dataset.iloc[1:]
    #at = at[:-1]
    tam = len(dataset['IDADE'])
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
    dataset[i]= 0
    
#atribuindo o valor de l0 para a primeira coluna de lx 
dataset['lx'].iloc[0] = l0
#%%
#preencher os valores em lx e dx
tam_2 = tam - 1
while c < tam:
    dataset['dx'] = dataset['lx'] * dataset[s]
    lx_2 =  dataset['lx'] - dataset['dx']
    lx_2 = lx_2.iloc[0:tam_2]
    dataset['lx'].iloc[1:] = lx_2
    c +=1

#%%

#preencher os valores em v^x
dataset['v^x'] = 1/((1+j)**dataset['IDADE'])

#%%
#preencher os valores em Dx e Nx
dataset['Dx'] = dataset['lx'] * dataset['v^x']

dataset['Nx'].iloc[0] = dataset['Dx'].sum()
c = 1
while c < tam:
    dataset['Nx'].iloc[c] = dataset['Dx'].iloc[c:tam].sum()
    c +=1
    
# %%
#preencher os valores em Cx e Mx
c = 0
while c < tam_2:
    dataset['Cx'].iloc[c] = dataset['dx'].iloc[c] * dataset['v^x'].iloc[c+1]
    c += 1
    


dataset['Mx'].iloc[0] = dataset['Cx'].sum()
c = 1
while c < tam:
    dataset['Mx'].iloc[c] = dataset['Cx'].iloc[c:tam].sum()
    c +=1
    
