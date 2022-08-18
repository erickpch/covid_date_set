#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import pandas as pd

#En train_data_path colocas la ubicacion de la carpeta de "train_data"

train_data_path = 'D:/Users/johnd/Documents/proyecto/imagenes/train_data'



def borrari(carpeta,name_image):
    
    file_path = (train_data_path+'/'+carpeta+'/'+name_image)    
    #Elimina la imagen
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("La imagen fue eliminada")
    else:
        print("La imagen no existe") 
    
# In[ ]:




