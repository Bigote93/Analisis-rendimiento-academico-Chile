# Lectura de datos 
# Autor: Diego Nalli
# Fecha: 2024-03-20

# ------------ IMPORTACIONES LIBRERIA ----------
import sys
import os

import pandas as pd
from sklearn.preprocessing import StandardScaler

# ------------ Incorporamos el path para poder importar las utilidades ------------
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# ------------ IMPORTACION MODULOS PROPIOS ------------
from Recursos.utilidades import Utilidades
util = Utilidades()

# ------------ VARIABLES GLOBALES ------------
year = 2002

# ------------ LECTURA DE DATAFRAME ORIGINAL ------------
df_rendimiento = util.getDataset(2002)

# ------------ GENERAR DATAFRAME DE ESTABLECIMIENTOS UNICOS DEL AÑO ------------ 
establecimientos = util.getEstablecimientosUnicos(dataframe=df_rendimiento, year=year)

# ------------ CAMBIAR EL TIPO DE DATO DE PROMEDIO ANUAL ------------
df_rendimiento = util.changeTypePromedio(dataframe=df_rendimiento, year=year)

# ------------ OBTENER DATAFRAME DE ANALISIS DE ESTUDIANTES ------------
df_rendimiento = util.getAnalisisAlumno(dataframe=df_rendimiento, year=2002)

# ------------ OBTENER PROMEDIO DE PROMEDIO_GENERAL_ANUAL por NOMBRE_ESTABLECIMIENTO ------------
df_promedio = util.getPromedioEstablecimiento(dataframe=df_rendimiento, year=year)
#ordenando por promedio
df_promedio = df_promedio.sort_values(by='PROMEDIO_GENERAL_ANUAL', ascending=False)
print(df_promedio.head(10))








