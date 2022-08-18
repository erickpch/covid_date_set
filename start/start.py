import json
import os
import zipfile

KAGGLE_PATH = "D:/proyecto/descargas"
API_PATH = "D:/proyecto"

def credenciales():    
    #esta funcion genera las credenciales de kaggle para iniciar culquier operacion
    os.mkdir(KAGGLE_PATH)
    api_token = {"username":"erickpc","key":"c414dbe542675528e1adaa8adc0dbe31"}
    with open(API_PATH + 'kaggle.json', 'w') as file:
        json.dump(api_token, file)
        
'''def descarga():    
    #Estafuncion descarga desde kaggle el paquete.
    os.chdir(KAGGLE_PATH)    
    !kaggle datasets download -d tawsifurrahman/covid19-radiography-database'''
    

def descompresion():
    if not os.path.exists('./imagenes'):
      os.makedirs('imagenes')
    with zipfile.ZipFile(KAGGLE_PATH + "/covid19-radiography-database.zip", 'r') as zip_ref:
        zip_ref.extractall(KAGGLE_PATH + '/images')


