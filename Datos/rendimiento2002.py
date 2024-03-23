# Lectura de datos 
# Autor: Diego Nalli
# Fecha: 2024-03-20

# ------------ IMPORTACIONES LIBRERIA ----------
import sys
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
df_rendimiento = util.getDataset(year=year)

# ------------ GENERAR DATAFRAME DE ESTABLECIMIENTOS UNICOS DEL AÑO ------------ 
establecimientos = util.getEstablecimientosUnicos(dataframe=df_rendimiento, year=year)

# ------------ CAMBIAR EL TIPO DE DATO DE PROMEDIO ANUAL ------------
df_rendimiento = util.changeTypePromedio(dataframe=df_rendimiento, year=year)

# ------------ OBTENER DATAFRAME DE ANALISIS DE ESTUDIANTES ------------
df_rendimiento = util.getAnalisisAlumno(dataframe=df_rendimiento, year=year)

# ------------ OBTENER PROMEDIO DE PROMEDIO_GENERAL_ANUAL por NOMBRE_ESTABLECIMIENTO ------------
df_promedio = util.getPromedioEstablecimiento(dataframe=df_rendimiento, year=year)

# ------------ GENERAR COLUMNAS DUMMY PARA VARIABLES CATEGORICAS ------------
df_rendimiento_dummies = util.getDummies(dataframe=df_rendimiento, year=year)

# ------------ OBTENER CORRELACION ENTRE COLUMNAS DEL DATAFAME SIN COLUMNA NOMBRE_ESTABLECIMIENTO------------
# df_ = df_rendimiento.drop(columns=['NOMBRE_ESTABLECIMIENTO', 'MASCARA_RUN_ALUMNO'])
# correlacion = df_.corr()
# print(correlacion[['ASISTENCIA_ANUAL']])

# ------------ GRAFICO DE GENERO Y DEPENDENCIA DEL ESTABLECIMIENTO POR REGION ------------
util.graficoGeneroDependencia(dataframe=df_rendimiento, year=year)

# ------------ GRAFICO DE PROMEDIO GENERAL ANUAL POR REGION ------------
util.graficoPromedioDependencia(dataframe=df_rendimiento, year=year)






