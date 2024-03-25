import pandas as pd
from Recursos.utilidades import Utilidades
util = Utilidades()

years = [i for i in range(2002 , 2015)]
for year in years:
    df_general = util.getDataset(year=year)
    print('Trabajando dataframe del año: ', year)
    df_general = util.changeTypePromedio(dataframe=df_general, year=year)
    df_promedio = util.getPromedioEstablecimiento(dataframe=df_general, year=year)
    df_establecimientos_unicos = util.getEstablecimientosUnicos(dataframe=df_general, year=year)
