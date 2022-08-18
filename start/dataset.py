import pandas as pd
import os


def create():
    TRAINSET_PATH = "D:/proyecto/imagenes/train_data"
    categories = ["COVID","Lung_Opacity","Normal","Viral Pneumonia"]
    
    index = []
    nombre = []
    formato = []
    categoria = []
    ancho = []
    alto = []
    URL = []
    contador=1
    
    for idx, category in enumerate(categories): 
        actual_path= TRAINSET_PATH + '/' + category
        a= os.listdir(actual_path)
        df= pd.DataFrame(a)    
        
        for i in range (len(df)):
            index.append(contador)
            contador= contador + 1
            nom, form = df.iloc[i][0].split(".")
            nombre.append(nom)
            formato.append(form)
            categoria.append(category)
            link= TRAINSET_PATH + '/' + category + '/' + df.iloc[i][0]
            URL.append(link)
        
    
    df = pd.DataFrame(index)
    df['Nombre'] = nombre
    df['Formato'] = formato
    df['Categoría'] = categoria
    df['URL'] = URL
    
    df.to_excel('D:/proyecto/dataset.xlsx')
    