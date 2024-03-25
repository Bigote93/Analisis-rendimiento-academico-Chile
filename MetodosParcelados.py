import pandas as pd
from Recursos.utilidades import Utilidades
util = Utilidades()
import random 

# --------- CREANDO DATAFRAMES DE PROMEDIOS Y ESTABLECIMIENTOS UNICOS DE LOS AÑOS 2002 A 2023 ---------
# years = [i for i in range(2002 , 2023)]
# for year in years:
#     df_general = util.getDataset(year=year)
#     print('Trabajando dataframe del año: ', year)
#     df_general = util.changeTypePromedio(dataframe=df_general, year=year)
#     df_promedio = util.getPromedioEstablecimiento(dataframe=df_general, year=year)
#     df_establecimientos_unicos = util.getEstablecimientosUnicos(dataframe=df_general, year=year)

# -------- CREANDO DATAFRAMES DE PROMEDIOS Y CODIGOS DE REGION DE LOS AÑOS 2002 A 2022 ---------
years = [i for i in range(2002 , 2023)]
for year in years:
    df_general = util.getDataset(year=year)
    print('Trabajando dataframe del año: ', year)
    df_general = util.changeTypePromedio(dataframe=df_general, year=year)
    df_promedio = util.getPromedioRegion(dataframe=df_general, year=year)


