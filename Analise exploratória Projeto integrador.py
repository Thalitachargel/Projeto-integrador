#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Baixar bibliotecas
import pandas as pd
import numpy as np
pd.options.display.max_rows = 999
pd.set_option("max_colwidth", 400)


# In[2]:


#importar dataset de treino
df_train = pd.read_csv("TrainingWiDS2021.csv")
df_train


# In[14]:


#Visualizar colunas
colunas = df_train.columns.values
colunas


# In[22]:


#Importar dicionario de dados
dicionario = pd.read_csv('DataDictionaryWiDS2021.csv')
dicionario


# #Lista Hipoteses:
# 
# -acidez do sangue
# -acidez da urina
# -lactate contration
# -creatina
# -glucose
# -hepatopatia
# -cirrose
# -bicarbonato 
# 
# dispensar medidas da 1h e Ficar so com as 24h.
# 

# In[ ]:


#verificar dados faltosos


# In[ ]:


#padronizar dados


# In[ ]:


#Colunas que devem ser dropadas 
colunas_drop = ("hospital_id",'elective_surgery', 'height', 'icu_id', 'hospital_admit_source', 'icu_admit_source','icu_admit_type','gcs_eyes_apache','gcs_motor_apache')

