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
rendimiento2006 = None
rendimiento2007 = None
rendimiento2008 = None
rendimiento2009 = None

# Cargamos los datasets
for idx, route in enumerate(variables.routes_dict):
    if 4<= idx < 8:  # Solo cargamos los primeros cuatro datasets
        try:
            rendimiento = pd.read_csv(route['route'], sep=';', encoding='latin1')
            print('Cargado el dataset del año:', route['year'])
            
            # Asignamos el DataFrame cargado a la variable correspondiente
            if idx == 4:
                rendimiento2006 = rendimiento
            elif idx == 5:
                rendimiento2007 = rendimiento
            elif idx == 6:
                rendimiento2008 = rendimiento
            elif idx == 7:
                rendimiento2009 = rendimiento
                
        except Exception as e:
            print('Error al cargar el dataset del año:', route['year'])
            print('Error:', e)

# Ahora puedes acceder a los DataFrames cargados
print(rendimiento2006.head(5))