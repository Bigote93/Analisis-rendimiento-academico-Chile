# Lectura de datos 
# Autor: Diego Nalli
# Fecha: 2024-03-20

# Importar librerías
import pandas as pd
import sys
import os

# Incorporamos el path para poder importar las utilidades
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Importamos las utilidades
from Recursos.utilidades import Utilidades
variables = Utilidades()

# Variables
rendimiento2002 = pd.DataFrame()

# Cargamos dataset
for element in variables.routes_dict:
    if element['year'] == 2002:
        try:
            
            rendimiento2002 = pd.read_csv(element['route'], sep=';', encoding='latin1')
            print('Cargado el dataset del año:', element['year'])
        except Exception as e:
            print('Error al cargar el dataset del año:', element['year'])
            print('Error:', e)

print(rendimiento2002.head(5))