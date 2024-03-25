import pandas as pd
from Recursos.utilidades import Utilidades
util = Utilidades()
import random 

# years = [i for i in range(2002 , 2015)]
# for year in years:
#     df_general = util.getDataset(year=year)
#     print('Trabajando dataframe del año: ', year)
#     df_general = util.changeTypePromedio(dataframe=df_general, year=year)
#     df_promedio = util.getPromedioEstablecimiento(dataframe=df_general, year=year)
#     df_establecimientos_unicos = util.getEstablecimientosUnicos(dataframe=df_general, year=year)


lista_numerica_prueba_azar = [random.randint(1, 100) for i in range(20)]
print(lista_numerica_prueba_azar)

lista_condicionada = [1 if i >= lista_numerica_prueba_azar[idx-1] else 0 for idx, i in enumerate(lista_numerica_prueba_azar)]
print(lista_condicionada)