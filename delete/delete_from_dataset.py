#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import pandas as pd


#En train_data_path colocas la ubicacion de la carpeta de "train_data"
train_data_path = 'D:/Users/johnd/Documents/proyecto/imagenes/train_data'

#Ubicacion del excel creado
excel_path = 'D:/Users/johnd/Documents/proyecto/dataset.xlsx'


def borrare(carpeta,name_image):
    
    file_path = (train_data_path+'/'+carpeta+'/'+name_image)
    df = pd.read_excel(excel_path)

    #Elimina la fila del dataframe leido del excel
    df = df.drop(df[df.URL == file_path].index)   

    #Elimina el viejo excel
    if os.path.isfile(excel_path):
        os.remove(excel_path)
        print("El excel fue eliminado")
    else:
        print("El excel no existe")
    
    #Se crea el nuevo excel
    df.to_excel('C:/Users/johnd/Documents/proyecto/dataset.xlsx')    
    
# In[ ]:




