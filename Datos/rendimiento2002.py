# Lectura de datos 
# Autor: Diego Nalli
# Fecha: 2024-03-20

# ------------ IMPORTACIONES LIBRERIA ----------
import sys
import os

import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler

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
print('Lectura de dataframe del año: ', year)
print('---------------------------------')


# ------------ GENERAR DATAFRAME DE ESTABLECIMIENTOS UNICOS DEL AÑO ------------ 
establecimientos = util.getEstablecimientosUnicos(dataframe=df_rendimiento, year=year)
print('Establecimientos unicos del año realizado')
print('---------------------------------')


# ------------ CAMBIAR EL TIPO DE DATO DE PROMEDIO ANUAL ------------
df_rendimiento = util.changeTypePromedio(dataframe=df_rendimiento, year=year)
print('Cambio de tipo de dato de promedio anual realizado')
print('---------------------------------')


# ------------ OBTENER DATAFRAME DE ANALISIS DE ESTUDIANTES ------------
df_rendimiento= util.getAnalisisAlumno(dataframe=df_rendimiento, year=year)
print('Analisis de alumnos realizado')
print('---------------------------------')


# ------------ OBTENER PROMEDIO DE PROMEDIO_GENERAL_ANUAL por NOMBRE_ESTABLECIMIENTO ------------
df_promedio = util.getPromedioEstablecimiento(dataframe=df_rendimiento, year=year)
print('Promedio de promedio general anual realizado')
print('---------------------------------')


# ------------ GENERAR COLUMNAS DUMMY PARA VARIABLES CATEGORICAS ------------
df_rendimiento_dummies = util.getDummies(dataframe=df_rendimiento, year=year)
print('Generacion de dummies realizada')
print('---------------------------------')


# ------------ OBTENER CORRELACION ENTRE COLUMNAS DEL DATAFAME SIN COLUMNA NOMBRE_ESTABLECIMIENTO------------
# df_ = df_rendimiento.drop(columns=['NOMBRE_ESTABLECIMIENTO', 'MASCARA_RUN_ALUMNO'])
# correlacion = df_.corr()
# print(correlacion[['ASISTENCIA_ANUAL']])

# ------------ GRAFICO DE GENERO Y DEPENDENCIA DEL ESTABLECIMIENTO POR REGION ------------
util.graficoGeneroDependencia(dataframe=df_rendimiento, year=year)
print('Grafico de genero y dependencia realizado')
print('---------------------------------')


# ------------ GRAFICO DE PROMEDIO GENERAL ANUAL POR REGION ------------
util.graficoPromedioDependencia(dataframe=df_rendimiento, year=year)
print('Grafico de promedio general anual por region realizado')
print('---------------------------------')


# ------------ MERGE DE DATAFRAME DE ESTABLECIMIENTOS CON DATAFRAME DE PROMEDIO GENERAL ANUAL ------------
merge_establecimientos = pd.DataFrame()
for ruta_promedio in util.routes_promedio:
    print('Incorporando dataframe: ', ruta_promedio['year'])
    df = pd.read_csv(ruta_promedio['route'])
    merge_establecimientos = pd.concat([merge_establecimientos, df], ignore_index=True)
    merge_establecimientos.to_csv('Estadisticas/Generales/promedioestablecimiento20022022.csv', index=False)


# ------------ CONSEGUIR REGISTROS DE merge_establecimientos EN QUE EL VALOR DE ROL_ESTABLECIMIENTO SEA 9967 ------------
rol_establecimiento = 9967
df_rol = merge_establecimientos[merge_establecimientos['ROL_ESTABLECIMIENTO'] == rol_establecimiento]
print('Registros con ROL_ESTABLECIMIENTO = 9967')
print(df_rol)







