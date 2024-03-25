# Funciones útiles para el manejo de archivos y directorios
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Rutas documentos
class Utilidades:

    def __init__(self):
        self.routes_dict = self.routes_dict


    routes_dict = [
        {'year': 2002, 'route': './Dataset/Rendimiento-2002/Rendimiento por estudiante 2002.csv',},
        {'year': 2003, 'route': './Dataset/Rendimiento-2003/Rendimiento por estudiante 2003.csv',},
        {'year': 2004, 'route': './Dataset/Rendimiento-2004/20130422_Rendimiento_2004_20050323_PUBL.csv',},
        {'year': 2005, 'route': './Dataset/Rendimiento-2005/Rendimiento por estudiante 2005.csv',},
        {'year': 2006, 'route': './Dataset/Rendimiento-2006/20130305_Rendimiento_2006_20070620_PUBL.csv',},
        {'year': 2007, 'route': './Dataset/Rendimiento-2007/Rendimiento por estudiante 2007.csv',},
        {'year': 2008, 'route': './Dataset/Rendimiento-2008/Rendimiento por estudiante 2008.csv',},
        {'year': 2009, 'route': './Dataset/Rendimiento-2009/Rendimiento por estudiante 2009.csv',},
        {'year': 2010, 'route': './Dataset/Rendimiento-2010/Rendimiento por estudiante 2010.csv',},
        {'year': 2011, 'route': './Dataset/Rendimiento-2011/Rendimiento por estudiante 2011.csv',},
        {'year': 2012, 'route': './Dataset/Rendimiento-2012/Rendimiento por estudiante 2012.csv',},
        {'year': 2013, 'route': './Dataset/Rendimiento-2013/Rendimiento por estudiante 2013.csv',},
        {'year': 2014, 'route': './Dataset/Rendimiento-2014/Rendimiento por estudiante 2014.csv',},
        {'year': 2015, 'route': './Dataset/Rendimiento-2015/Rendimiento por estudiante 2015.csv',},
        {'year': 2016, 'route': './Dataset/Rendimiento-2016/20170216_Rendimiento_2016_20170131_PUBL.csv',},
        {'year': 2017, 'route': './Dataset/Rendimiento-2017/20180213_Rendimiento_2017_20180131_PUBL.csv',},
        {'year': 2018, 'route': './Dataset/Rendimiento-2018/20190220_Rendimiento_2018_20190131_PUBL.csv',},
        {'year': 2019, 'route': './Dataset/Rendimiento-2019/20200220_Rendimiento_2019_20200131_PUBL.csv',},
        {'year': 2020, 'route': './Dataset/Rendimiento-2020/20210223_Rendimiento_2020_20210131_WEB.csv',},
        {'year': 2021, 'route': './Dataset/Rendimiento-2021/20220302_Rendimiento_2021_20220131_WEB.csv',},
        {'year': 2022, 'route': './Dataset/Rendimiento-2022/20230209_Rendimiento_2022_20230131_WEB.csv',}
    ]


    routes_promedio = [
        {'year': 2002, 'route': './Estadisticas/2002/promedio_establecimiento2002.csv',},
        {'year': 2003, 'route': './Estadisticas/2003/promedio_establecimiento2003.csv',},
        {'year': 2004, 'route': './Estadisticas/2004/promedio_establecimiento2004.csv',},
        {'year': 2005, 'route': './Estadisticas/2005/promedio_establecimiento2005.csv',},
        {'year': 2006, 'route': './Estadisticas/2006/promedio_establecimiento2006.csv',},
        {'year': 2007, 'route': './Estadisticas/2007/promedio_establecimiento2007.csv',},
        {'year': 2008, 'route': './Estadisticas/2008/promedio_establecimiento2008.csv',},
        {'year': 2009, 'route': './Estadisticas/2009/promedio_establecimiento2009.csv',},
        {'year': 2010, 'route': './Estadisticas/2010/promedio_establecimiento2010.csv',},
        {'year': 2011, 'route': './Estadisticas/2011/promedio_establecimiento2011.csv',},
        {'year': 2012, 'route': './Estadisticas/2012/promedio_establecimiento2012.csv',},
        {'year': 2013, 'route': './Estadisticas/2013/promedio_establecimiento2013.csv',},
        {'year': 2014, 'route': './Estadisticas/2014/promedio_establecimiento2014.csv',},
        {'year': 2015, 'route': './Estadisticas/2015/promedio_establecimiento2015.csv',},
        {'year': 2016, 'route': './Estadisticas/2016/promedio_establecimiento2016.csv',},
        {'year': 2017, 'route': './Estadisticas/2017/promedio_establecimiento2017.csv',},
        {'year': 2018, 'route': './Estadisticas/2018/promedio_establecimiento2018.csv',},
        {'year': 2019, 'route': './Estadisticas/2019/promedio_establecimiento2019.csv',},
        {'year': 2020, 'route': './Estadisticas/2020/promedio_establecimiento2020.csv',},
        {'year': 2021, 'route': './Estadisticas/2021/promedio_establecimiento2021.csv',},
        {'year': 2022, 'route': './Estadisticas/2022/promedio_establecimiento2022.csv',}
    ]

    # Nombre de columnas
    map_columns = {
        'AGNO': 'AÑO','agno': 'AÑO',
        'RBD': 'ROL_ESTABLECIMIENTO','rbd': 'ROL_ESTABLECIMIENTO',
        'DGV_RBD':'DIGITO_VERIFICADOR_RBD','dgv_rbd':'DIGITO_VERIFICADOR_RBD',
        'NOM_RBD': 'NOMBRE_ESTABLECIMIENTO','nom_rbd': 'NOMBRE_ESTABLECIMIENTO',
        'LET_RBD': 'LETRA_ESTABLECIMIENTO','let_rbd': 'LETRA_ESTABLECIMIENTO',
        'NUM_RBD':'NUMERO_ESTABLECIMIENTO','num_rbd':'NUMERO_ESTABLECIMIENTO',
        'COD_REG_RBD': 'CODIGO_REGION_ESTABLECIMIENTO','cod_reg_rbd': 'CODIGO_REGION_ESTABLECIMIENTO',
        'NOM_REG_RBD_A': 'NOMBRE_ABREV_REGION_ESTABLECIMIENTO','nom_reg_rbd_a': 'NOMBRE_ABREV_REGION_ESTABLECIMIENTO',
        'COD_PRO_RBD': 'CODIGO_OFICIAL_PROVINCIA_ESTABLECIMIENTO','cod_pro_rbd': 'CODIGO_OFICIAL_PROVINCIA_ESTABLECIMIENTO',
        'COD_COM_RBD': 'CODIGO_OFICIAL_COMUNA_ESTABLECIMIENTO','cod_com_rbd': 'CODIGO_OFICIAL_COMUNA_ESTABLECIMIENTO',
        'NOM_COM_RBD': 'NOMBRE_COMUNA_ESTABLECIMIENTO','nom_com_rbd': 'NOMBRE_COMUNA_ESTABLECIMIENTO',
        'COD_DEPROV_RBD':'CODIGO_DEPARTAMENTO_PROVINCIAL_ESTABLECIMIENTO','cod_deprov_rbd':'CODIGO_DEPARTAMENTO_PROVINCIAL_ESTABLECIMIENTO',
        'NOM_DEPROV_RBD':'NOMBRE_DEPARTAMENTO_PROVINCIAL_ESTABLECIMIENTO','nom_deprov_rbd':'NOMBRE_DEPARTAMENTO_PROVINCIAL_ESTABLECIMIENTO',
        'COD_DEPE':'CODIGO_DEPENDENCIA_ESTABLECIMIENTO','cod_depe':'CODIGO_DEPENDENCIA_ESTABLECIMIENTO',
        'COD_DEPE2':'CODIGO_DEPENDENCIA_ESTABLECIMIENTO_GRUP','cod_depe2':'CODIGO_DEPENDENCIA_ESTABLECIMIENTO_GRUP',
        'RURAL_RBD':'INDICE_RURALIDAD_ESTABLECIMIENTO','rural_rbd':'INDICE_RURALIDAD_ESTABLECIMIENTO',
        'ESTADO_ESTAB':'ESTADO_ESTABLECIMIENTO','estado_estab':'ESTADO_ESTABLECIMIENTO',
        'COD_ENSE':'CODIGO_ENSENANZA_ESTABLECIMIENTO','cod_ense':'CODIGO_ENSENANZA_ESTABLECIMIENTO',
        'COD_ENSE2':'NIVEL_ENSEÑANZA_GRUP','cod_ense2':'NIVEL_ENSEÑANZA_GRUP',
        'COD_GRADO':'CODIGO_GRADO_ESTABLECIMIENTO','cod_grado':'CODIGO_GRADO_ESTABLECIMIENTO',
        'LET_CUR':'LETRA_CURSO','let_cur':'LETRA_CURSO',
        'COD_JOR':'JORNADA_ESTABLECIMIENTO','cod_jor':'JORNADA_ESTABLECIMIENTO',
        'COD_TIP_CUR':'INDICE_TIPO_CURSO','cod_tip_cur':'INDICE_TIPO_CURSO',
        'COD_DES_CUR':'DESCRIPCION_CURSO','cod_des_cur':'DESCRIPCION_CURSO',
        'MRUN':'MASCARA_RUN_ALUMNO','mrun':'MASCARA_RUN_ALUMNO',
        'GEN_ALU':'GENERO_ALUMNO','gen_alu':'GENERO_ALUMNO',
        'FEC_NAC_ALU':'FECHA_NACIMIENTO_ALUMNO','fec_nac_alu':'FECHA_NACIMIENTO_ALUMNO',
        'EDAD_ALU':'EDAD_ALUMNO','edad_alu':'EDAD_ALUMNO',
        'INT_ALU':'INDICADOR_ALUMNO','int_alu':'INDICADOR_ALUMNO',
        'GD_ALU':'CONDICION_DIFERENCIAL_ALUMNO','gd_alu':'CONDICION_DIFERENCIAL_ALUMNO',
        'COD_REG_ALU':'CODIGO_REGION_ALUMNO','cod_reg_alu':'CODIGO_REGION_ALUMNO',
        'COD_COM_ALU':'CODIGO_COMUNA_ALUMNO','cod_com_alu':'CODIGO_COMUNA_ALUMNO',
        'NOM_COM_ALU':'NOMBRE_COMUNA_ALUMNO','nom_com_alu':'NOMBRE_COMUNA_ALUMNO',
        'COD_RAMA':'CODIGO_RAMA','cod_rama':'CODIGO_RAMA',
        'COD_SEC':'CODIGO_SECTOR_ECONOMICO','cod_sec':'CODIGO_SECTOR_ECONOMICO',
        'COD_ESPE':'CODIGO_ESPECIALIDAD','cod_espe':'CODIGO_ESPECIALIDAD',
        'FECH_ING_ALU':'FECHA_INGRESO_ALUMNO','fech_ing_alu':'FECHA_INGRESO_ALUMNO',
        'PROM_GRAL':'PROMEDIO_GENERAL_ANUAL','prom_gral':'PROMEDIO_GENERAL_ANUAL',
        'ASISTENCIA':'ASISTENCIA_ANUAL','asistencia':'ASISTENCIA_ANUAL',
        'SIT_FIN':'SITUACION_PROMOCION','sit_fin':'SITUACION_PROMOCION',
        'SIT_FIN_R':'SITUACION_PROMOCION_TRASLADO','sit_fin_r':'SITUACION_PROMOCION_TRASLADO',
        'COD_MEN':'MENCION', 'cod_men':'MENCION'
        
    }

    # Mapa de codigo region (COD_REG_RBD)
    map_region = {
        1: 'Región de Tarapacá',
        2: 'Región de Antofagasta',
        3: 'Región de Atacama',
        4: 'Región de Coquimbo',
        5: 'Región de Valparaíso',
        6: 'Región del Libertador General Bernardo O’Higgins',
        7: 'Región del Maule',
        8: 'Región del Biobío',
        9: 'Región de La Araucanía',
        10: 'Región de Los Lagos',
        11: 'Región de Aysén del General Carlos Ibáñez del Campo',
        12: 'Región de Magallanes y de la Antártica Chilena',
        13: 'Región Metropolitana de Santiago',
        14: 'Región de Los Ríos',
        15: 'Región de Arica y Parinacota',
        16: 'Región de Ñuble'
    }

    # Mapa de codigo provincia (COD_PRO_RBD)
    map_provincia = {
        11:  'Provincia de Iquique',
        14:  'Provincia del Tamarugal',
        21:  'Provincia de Antofagasta',
        22:  'Provincia de El Loa',
        23:  'Provincia de Tocopilla',
        31:  'Provincia de Copiapó',
        32:  'Provincia de Chañaral',
        33:  'Provincia de Huasco',
        41:  'Provincia de Elqui',
        42:  'Provincia de Choapa',
        43:  'Provincia de Limarí',
        51:  'Provincia de Valparaíso',
        52:  'Provincia de Isla de Pascua',
        53:  'Provincia de Los Andes',
        54:  'Provincia de Petorca',
        55:  'Provincia de Quillota',
        56:  'Provincia de San Antonio',
        57:  'Provincia de San Felipe de Aconcagua',
        58:  'Provincia de Marga Marga',
        61:  'Provincia de Cachapoal',
        62:  'Provincia de Cardenal Caro',
        63:  'Provincia de Colchagua',
        71:  'Provincia de Talca',
        72:  'Provincia de Cauquenes',
        73:  'Provincia de Curicó',
        74:  'Provincia de Linares',
        81:  'Provincia de Concepción',
        82:  'Provincia de Arauco',
        83:  'Provincia de Biobío',
        84:  'Provincia de Ñuble',
        91:  'Provincia de Cautín',
        92:  'Provincia de Malleco',
        101: 'Provincia de Llanquihue',
        102: 'Provincia de Chiloé',
        103: 'Provincia de Osorno',
        104: 'Provincia de Palena',
        111: 'Provincia de Coyhaique',
        112: 'Provincia de Aysén',
        113: 'Provincia de Capitán Prat',
        114: 'Provincia de General Carrera',
        121: 'Provincia de Magallanes',
        122: 'Provincia de Antártica Chilena',
        123: 'Provincia de Tierra del Fuego',
        124: 'Provincia de Última Esperanza',
        131: 'Provincia de Santiago',
        132: 'Provincia de Cordillera',
        133: 'Provincia de Chacabuco',
        134: 'Provincia de Maipo',
        135: 'Provincia de Melipilla',
        136: 'Provincia de Talagante',
        141: 'Provincia de Valdivia',
        142: 'Provincia de Ranco',
        151: 'Provincia de Arica',
        152: 'Provincia de Parinacota',
        161: 'Provincia de Diguillín',
        162: 'Provincia de Itata',
        163: 'Provincia de Punilla'
    }

    # Mapa codigo enseñanza (COD_ENSE)
    map_enseñanza = {
        110: 'Enseñanza Básica',
        160: 'Educación Básica Común Adultos (Decreto 584/2007)',
        161: 'Educación Básica Especial Adultos',
        163: 'Escuelas Cárceles (Básica Adultos)',
        165: 'Educación Básica Adultos Sin Oficios (Decreto 584/2007)',
        167: 'Educación Básica Adultos Con Oficios (Decreto 584/2007 y 999/2009)',
        310: 'Enseñanza Media H-C niños y jóvenes',
        360: 'Educación Media H-C adultos vespertino y nocturno (Decreto 190/1975)',
        361: 'Educación Media H-C adultos (Decreto 12/1987)',
        362: 'Escuelas Cárceles (Media Adultos)',
        363: 'Educación Media H-C Adultos (Decreto 1000/2009)',
        410: 'Enseñanza Media T-P Comercial Niños y Jóvenes',
        460: 'Educación Media T-P Comercial Adultos (Decreto 152/1989)',
        461: 'Educación Media T-P Comercial Adultos (Decreto 152/1989)',
        463: 'Educación Media T-P Comercial Adultos (Decreto 1000/2009)',
        510: 'Enseñanza Media T-P Industrial Niños y Jóvenes',
        560: 'Educación Media T-P Industrial Adultos (Decreto 152/1989)',
        561: 'Educación Media T-P Industrial Adultos (Decreto 152/1989)',
        563: 'Educación Media T-P Industrial Adultos (Decreto 1000/2009)',
        610: 'Enseñanza Media T-P Técnica Niños y Jóvenes',
        660: 'Educación Media T-P Técnica Adultos (Decreto 152/1989)',
        661: 'Educación Media T-P Técnica Adultos (Decreto 152/1989)',
        663: 'Educación Media T-P Técnica Adultos (Decreto 1000/2009)',
        710: 'Enseñanza Media T-P Agrícola Niños y Jóvenes',
        760: 'Educación Media T-P Agrícola Adultos (Decreto 152/1989)',
        761: 'Educación Media T-P Agrícola Adultos (Decreto 152/1989)',
        763: 'Educación Media T-P Agrícola Adultos (Decreto 1000/2009)',
        810: 'Enseñanza Media T-P Marítima Niños y Jóvenes',
        860: 'Enseñanza Media T-P Marítima Adultos (Decreto 152/1989)',
        863: 'Enseñanza Media T-P Marítima Adultos (Decreto 1000/2009)',
        910: 'Enseñanza Media Artística Niños y Jóvenes',
        963: 'Enseñanza Media Artística Adultos'
    }

    # Mapa codigo enseñanza (COD_ENSE2)
    map_nivel_enseñanza = {
        2: 'Enseñanza Básica Niños',
        3: 'Enseñanza Basica Adultos',
        5: 'Enseñanza Media Humanístico Científica Jovenes',
        6: 'Enseñanza Media Humanístico Científica Adultos',
        7: 'Enseñanza Media Técnico Profesional y Artística Jovenes',
        8: 'Enseñanza Media Técnico Profesional y Artística Adultos'
    }

    # Mapa grados tipo enseñanza (COD_GRADO) por nivel de enseñanza (COD_ENSE)
    map_grado = {
        110-1: '1° Básico', 
        110-2: '2° Básico', 
        110-3: '3° Básico', 
        110-4: '4° Básico', 
        110-5: '5° Básico', 
        110-6: '6° Básico', 
        110-7: '7° Básico', 
        110-8: '8° Básico',

        160-1: 'Alfabetización',
        160-2: 'Nivel Básico 1 (1° a 4° Básico)', 
        160-3: 'Nivel Básico 2 (5° a 6° Básico)', 
        160-4: 'Nivel Básico 3 (7° a 8° Básico)', 
        160-5: 'Nivel Técnico',

        161-1: 'Alfabetización', 
        161-2: 'Nivel Básico 1 (1° a 4° Básico)', 
        161-3: 'Nivel Básico 2 (5° a 6° Básico)', 
        161-4: 'Nivel Básico 3 (7° a 8° Básico)', 
        161-5: 'Nivel Técnico',

        163-1: 'Alfabetización', 
        163-2: 'Nivel Básico 1 (1° a 4° Básico)', 
        163-3: 'Nivel Básico 2 (5° a 6° Básico)', 
        163-4: 'Nivel Básico 3 (7° a 8° Básico)', 
        163-5: 'Nivel Técnico',

        165-1: 'Nivel Básico 1 (1° a 4° Básico)', 
        165-2: 'Nivel Básico 2 (5° a 6° Básico)', 
        165-3: 'Nivel Básico 3 (7° a 8° Básico)', 

        167-2: 'Nivel Básico 2 (5° a 6° Básico)', 
        167-3: 'Nivel Básico 3 (7° a 8° Básico)',

        310-1: '1° Medio', 
        310-2: '2° Medio', 
        310-3: '3° Medio', 
        310-4: '4° Medio',

        360-1: '1° Medio', 
        360-2: '2° Medio', 
        360-3: '3° Medio', 
        360-4: '4° Medio',

        361-1: 'Primer ciclo (1° y 2° Medio)', 
        361-3: 'Segundo ciclo (3° y 4° Medio)',

        363-1: 'Primer nivel (1° y 2° Medio)', 
        363-3: 'Segundo nivel (3° y 4° Medio)',

        410-1: '1° Medio', 
        410-2: '2° Medio', 
        410-3: '3° Medio', 
        410-4: '4° Medio',

        460-1: 'Primer ciclo (1° y 2° Medio)', 460-3: '3° Medio', 460-4: '4° Medio',

        461-1: 'Primer ciclo (1° y 2° Medio)', 461-3: '3° Medio', 461-4: '4° Medio',

        463-1: 'Primer nivel (1° y 2° Medio)', 463-3: 'Segundo nivel (3° Medio)', 463-4: 'Tercero nivel (4° Medio)',

        510-1: '1° Medio', 510-2: '2° Medio', 510-3: '3° Medio', 510-4: '4° Medio',

        560-1: 'Primer ciclo (1° y 2° Medio)', 560-3: '3° Medio', 560-4: '4° Medio',

        561-1: 'Primer ciclo (1° y 2° Medio)', 561-3: '3° Medio', 561-4: '4° Medio',

        563-1: 'Primer nivel (1° y 2° Medio)', 563-3: 'Segundo nivel (3° Medio)', 563-4: 'Tercero nivel (4° Medio)',

        610-1: '1° Medio', 610-2: '2° Medio', 610-3: '3° Medio', 610-4: '4° Medio',

        660-1: 'Primer ciclo (1° y 2° Medio)', 660-3: '3° Medio', 660-4: '4° Medio',

        661-1: 'Primer ciclo (1° y 2° Medio)', 661-3: '3° Medio', 661-4: '4° Medio',

        663-1: 'Primer nivel (1° y 2° Medio)', 663-3: 'Segundo nivel (3° Medio)', 663-4: 'Tercero nivel (4° Medio)',

        710-1: '1° Medio', 710-2: '2° Medio', 710-3: '3° Medio', 710-4: '4° Medio',

        760-1: 'Primer ciclo (1° y 2° Medio)', 760-3: '3° Medio', 760-4: '4° Medio',

        761-1: 'Primer ciclo (1° y 2° Medio)', 761-3: '3° Medio', 761-4: '4° Medio',

        763-1: 'Primer nivel (1° y 2° Medio)', 763-3: 'Segundo nivel (3° Medio)', 763-4: 'Tercero nivel (4° Medio)',

        810-1: '1° Medio', 810-2: '2° Medio', 810-3: '3° Medio', 810-4: '4° Medio',

        860-1: 'Primer ciclo (1° y 2° Medio)', 860-3: '3° Medio', 860-4: '4° Medio',

        863-1: 'Primer nivel (1° y 2° Medio)', 863-3: 'Segundo nivel (3° Medio)', 863-4: 'Tercero nivel (4° Medio)',

        910-1: '1° Medio', 910-2: '2° Medio', 910-3: '3° Medio', 910-4: '4° Medio',

        963-1: 'Segundo nivel (3° medio)', 963-2: 'Tercero nivel (4° medio)'

    }

    # Mapa rama de enseñanza (COD_RAMA)
    map_rama = {
        0: 'Ciclo General / Sin información',
        400: 'Comercial',
        500: 'Industrial',
        600: 'Técnica',
        700: 'Agrícola',
        800: 'Marítima',
        900: 'Artística'
    }

    # Map sector económico (COD_SEC)
    map_sector = {
        410: 'Administración y Comercio',
        510: 'Construcción',
        520: 'Metalmecánico',
        530: 'Electricidad',
        540: 'Minero',
        550: 'Gráfica',
        560: 'Químico',
        570: 'Confección',
        580: 'Tecnológia y Telecomunicaciones',
        610: 'Alimentación',
        620: 'Programas y Proyectos Sociales',
        630: 'Hoteleria y Turismo',
        640: 'Salud y Educación',
        710: 'Maderero',
        720: 'Agropecuario',
        810: 'Maritimo',
        910: 'Artes Visuales',
        920: 'Artes Escénicas Teatro',
        930: 'Artes Escénicas Danza',
    }

    # Mapa especialidad (COD_ESPE)
    map_especialidad = {
        41001: 'Administración', 41002: 'Contabilidad', 41003: 'Secretariado', 41004: 'Ventas', 41005: 'Administración (con mención)',

        51001: 'Edificación', 51002: 'Terminaciones de Construcción', 51003: 'Montaje Industrial', 51004: 'Obras viales y de infraestructura',
        51005: 'Instalacones Sanitarias', 51006: 'Refrigeración y Climatización', 51008: 'Instalaciones Sanitarias', 51009: 'Construcción (con mención)',

        52008: 'Mechánica Industrial', 52009: 'Construcciones Metálicas', 52010: 'Mecaánica Automotriz', 52011: 'Matricería',
        52012: 'Mecánica de mantención de aeronaves', 52013: 'Mecánica industrial (con mención)',

        53014: 'Electricidad', 53015: 'Electrónica', 53016: 'Telecomunicaciones',

        54018: 'Explotación Minera', 54019: 'Metalurgia Extractiva', 54020: 'Asistencia de Geología',

        55022: 'Gráfica', 55023: 'Dibujo Técnico',

        56025: 'Operacion de Plantas Químicas', 56026: 'Laboratorio Químico', 56027: 'Química Industrial (con mención)',

        57028: 'Tejido', 57029: 'Textil', 57030: 'Vestuario y Confección Textil', 57031: 'Productos del Cuero',

        58033: 'Conectividad y Redes', 58034: 'Programación', 58035: 'Telecomunicaciones',

        61001: 'Elaboración Industrial de Alimentos', 61002: 'Servicios de Alimentación Colectiva', 61003: 'Gastronomía (con mención)',

        62004: 'Atención de Párvulos', 62005: 'Atención de Adultos Mayores', 62006: 'Atención de Enfermeria', 
        62007: 'Atención Social y Recreativa', 62008: 'Atención de Enfermeria (con mención)',

        63009: 'Servicios de Turismo', 63010: 'Servicios Hoteleros', 63011: 'Servicios de Hoteleria',

        64001: 'Atención de Párvulos', 64008: 'Atención de Enfermeria (con mención)',

        71001: 'Forestal', 71002: 'Procesamiento de la Madera', 71003: 'Productos de la Madera', 71004: 'Celuosa y Papel', 71005: 'Muebles y Terminaciones de la Madera',
        
        72006: 'Agropecuaria', 72007: 'Agropecuaria (con mención)',

        81001: 'Naves mercantes y especiales', 81002: 'Pesqueria', 81003: 'Acuicultura', 81004: 'Operacion Portuaria', 81005: 'Tripulación de Naves Mercantes y Especiales',

        91001: 'Artes Visuales', 91002: 'Artes audiovisuales', 91003: 'Diseño', 91004: 'Artes Musicales', 91005: 'Artes escénicas',

        92004: 'Interpretación Teatral', 92005: 'Diseño Escénico',

        93006: 'Interpretación en Danza de Nivel Intermedio', 93007: 'Monitoria de Danza',
    }

    # Mapa de menciones (COD_MEN)
    map_mencion = {
        41005-41005001: 'Plan Comun',
        41005-41005002: 'Logistica',
        41005-41005003: 'Recursos Humanos',

        51009-51007001: 'Plan Comun',
        51009-51007002: 'Edificación',
        51009-51007003: 'Terminaciones de la Construcción',
        51009-51007004: 'Obra Viales e Infraestructura',

        52013-52013001: 'Plan Comun',
        52013-52013002: 'Mantenimiento Electromecánico',
        52013-52013003: 'Maquinas-Herramientas',
        52013-52013004: 'Matricería',

        56027-56027001: 'Plan Comun',
        56027-56027002: 'Planta Química',
        56027-56027003: 'Laboratorio Químico',

        61003-61003001: 'Plan Comun',
        61003-61003002: 'Cocina',
        61003-61003003: 'Pastelería y Repostería',

        64008-64008001: 'Adultos Mayores',
        64008-64008002: 'Enfermeria',
        64008-64008003: 'Plan Comun',

        72007-72007001: 'Plan Comun',
        72007-72007002: 'Agricultura',
        72007-72007003: 'Pecuaria',
        72007-72007004: 'Vitivinicola',
    }

    # Mapa de dependencia (COD_DEPE)
    map_dependencia = {
        1: 'Corporacion Municipal',
        2: 'Municipal DAEM',
        3: 'Particular subvencionado',
        4: 'Particular pagado (no subvencionado)',
        5: 'Corporacion de administracion delegada',
        6: 'Servicio local de educacion'
    }

    # Mapa indice ruralidzd del establecimiento
    map_ruralidad = {
        0: 'Urbano',
        1: 'Rural'
    }

    # Mapa estado establecimiento
    map_estado = {
        1: 'Funcionando',
        2: 'En receso',
        3: 'Cerrado',
        4: 'Autorizado sin matricula'
    }

    # Mapa jornada que asiste a clases estudiante
    map_jornada = {
        1: 'Mañana',
        2: 'Tarde',
        3: 'Mañana y tarde',
        4: 'Vespertina / nocturna'
    }

    # Mapa tipo curso
    map_tipocurso = {
        0: 'Curso simple',
        '1-6': 'Curso combinado'
    }

    # Mapa descripcion curso
    map_descripcion = {
        0: 'No Aplica',
        1: 'Solo liceo',
        2: 'Dual',
        3: 'Otro'
    }

    # Mapa genero estudiante
    map_genestu = {
        0: 'Sin informacion',
        1: 'Masculino',
        2: 'Femenino'
    }



    # Funcion que carga los dataset de rendimiento 
    def getDataset(self, year):
        for element in self.routes_dict:
            if element['year'] == year:
                try:
                    rendimiento = pd.read_csv(element['route'], sep=';', encoding='latin1')

                    # Cambio de nombre de columnas
                    rendimiento = rendimiento.rename(columns=self.map_columns)
                    rendimiento.to_csv('Estadisticas/'+str(year)+'/rendimiento'+str(year)+'.csv')

                    # Almacenar estadisticas en un archivo .csv
                    descripcion_estats = rendimiento.describe()
                    descripcion_estats.to_csv('Estadisticas/'+str(year)+'/rendimiento'+str(year)+'_descripcion.csv', index=False)

                    return rendimiento

                except Exception as e:
                    print('Error al cargar el dataset del año:', element['year'])
                    print('Error:', e)
                    return None
                
    # Funcion para obtener las escuelas unicas de un año (NOMBRE_ESTABLECIMIENTO, ROL_ESTABLECIMIENTO)
    def getEstablecimientosUnicos(self, dataframe, year):
        try:
            rendimiento = dataframe
            return rendimiento[['NOMBRE_ESTABLECIMIENTO', 'ROL_ESTABLECIMIENTO']].drop_duplicates()
        except Exception as e:
            print('Error al determinar los establecimientos unicos del año:', year)
            print('Error:', e)
            return None
    
    # Funcion para obtener columnas de analisis de alumno
    ## Columnas de interes:
        ## NOMBRE_ESTABLECIMIENTO
        ## CODIGO_REGION_ESTABLECIMIENTO
        ## CODIGO_OFICIAL_COMUNA_ESTABLECIMIENTO
        ## CODIGO_DEPENDENCIA_ESTABLECIMIENTO
        ## CODIGO_ENSENANZA_ESTABLECIMIENTO
        ## CODIGO_GRADO_ESTABLECIMIENTO
        ## GENERO_ALUMNO
        ## CODIGO_COMUNA_ALUMNO
        ## PROMEDIO_GENERAL_ANUAL
        ## ASISTENCIA_ANUAL
        ## MASCARA_RUN_ALUMNO
    def getAnalisisAlumno(self, dataframe, year):
        
        try:
            rendimiento = dataframe
            analisis_estudiante = rendimiento[[
                'NOMBRE_ESTABLECIMIENTO', 'CODIGO_REGION_ESTABLECIMIENTO', 'CODIGO_OFICIAL_COMUNA_ESTABLECIMIENTO', 
                'CODIGO_DEPENDENCIA_ESTABLECIMIENTO', 'CODIGO_ENSENANZA_ESTABLECIMIENTO', 'CODIGO_GRADO_ESTABLECIMIENTO', 
                'GENERO_ALUMNO', 'CODIGO_COMUNA_ALUMNO', 'PROMEDIO_GENERAL_ANUAL', 'ASISTENCIA_ANUAL','MASCARA_RUN_ALUMNO',
                'ROL_ESTABLECIMIENTO'
                ]]
            
            # Almacenar dataset en un archivo .csv
            analisis_estudiante.to_csv('Estadisticas/'+str(year)+'/analisis_estudiante'+str(year)+'.csv', index=False)

            return analisis_estudiante
        except Exception as e:
            print('Error al obtener el dataframe de analisis de alumno del año:', year)
            print('Error:', e)
            return None


    
    # Funcion para cambiar el tipo de dato de la columna PROMEDIO_GENERAL_ANUAL
    def changeTypePromedio(self, dataframe, year):
        
        try:
            rendimiento = dataframe
            rendimiento['PROMEDIO_GENERAL_ANUAL'] = rendimiento['PROMEDIO_GENERAL_ANUAL'].apply(lambda x: float(x.replace(',', '.')) if x is not None else None)
            return rendimiento
        except Exception as e:
            print('Error al cambiar el tipo de dato de los promedios:', year)
            print('Error:', e)
            return None
    
    # Funcion para obtener el promedio de PROMEDIO_GENERAL_ANUAL por NOMBRE_ESTABLECIMIENTO
    def getPromedioEstablecimiento(self, dataframe, year):
        try:
            rendimiento = dataframe
            promedio_establecimiento = rendimiento.groupby(['ROL_ESTABLECIMIENTO','NOMBRE_ESTABLECIMIENTO'])['PROMEDIO_GENERAL_ANUAL'].mean().reset_index()
            
            # Agregar columna de año
            promedio_establecimiento['ANIO'] = year
            
            # Ordenar de forma descendente
            promedio_establecimiento = promedio_establecimiento.sort_values('PROMEDIO_GENERAL_ANUAL', ascending=False)

            # Almacenar dataset en un archivo .csv
            promedio_establecimiento.to_csv('Estadisticas/'+str(year)+'/promedio_establecimiento'+str(year)+'.csv', index=False)
            return promedio_establecimiento
        except Exception as e:
            print('Error al obtener el promedio de promedio por establecimiento del año:', year)
            print('Error:', e)
            return None
        
    # Funcion para generar columnas dummy para las columnas:
        ## CODIGO_REGION_ESTABLECIMIENTO
        ## CODIGO_DEPENDENCIA_ESTABLECIMIENTO
        ## CODIGO_GRADO_ESTABLECIMIENTO
        ## GENERO_ALUMNO
    def getDummies(self, dataframe, year):

        # Mapa de columnas y prefix
        map_columns = {
            'CODIGO_REGION_ESTABLECIMIENTO': 'REGION',
            'CODIGO_DEPENDENCIA_ESTABLECIMIENTO': 'DEPENDENCIA',
            'CODIGO_GRADO_ESTABLECIMIENTO': 'GRADO',
            'GENERO_ALUMNO': 'GENERO'
        }

        try:
            rendimiento = dataframe
            
            for column in map_columns.keys():
                dummies = pd.get_dummies(rendimiento[column], prefix=map_columns[column]).astype(int)
                rendimiento = rendimiento.drop(column, axis=1)
                rendimiento = pd.concat([rendimiento, dummies], axis=1)
            
            # Almacenar dataset en un archivo .csv
            rendimiento.to_csv('Estadisticas/'+str(year)+'/rendimiento_dummies'+str(year)+'.csv', index=False)
            return rendimiento

        except Exception as e:
            print('Error al generar las columnas dummy del año:', year)
            print('Error:', e)
            return None
    
    # Funcion para graficar genero y dependencia del establecimiento por region
    def graficoGeneroDependencia(self, dataframe, year):
        df_trabajar = dataframe[[
            'GENERO_ALUMNO',
            'CODIGO_DEPENDENCIA_ESTABLECIMIENTO',
        ]]

        # CAMBIAR REGISTROS POR MAPA DE GENERO Y DEPENDENCIA
        df_trabajar['GENERO_ALUMNO'] = df_trabajar['GENERO_ALUMNO'].map(self.map_genestu)
        df_trabajar['CODIGO_DEPENDENCIA_ESTABLECIMIENTO'] = df_trabajar['CODIGO_DEPENDENCIA_ESTABLECIMIENTO'].map(self.map_dependencia)

        # AGRUPAMOS POR GENERO Y DEPENDENCIA
        df_trabajar = df_trabajar.groupby(['GENERO_ALUMNO', 'CODIGO_DEPENDENCIA_ESTABLECIMIENTO']).size().reset_index()
        df_trabajar.columns = ['GENERO_ALUMNO', 'CODIGO_DEPENDENCIA_ESTABLECIMIENTO', 'TOTAL']

        # ASIGNACION TAMAÑO GRAFICO
        plt.figure(figsize=(12, 8))

        # Definir una paleta de colores personalizada para los géneros
        #palette = {'Canadá': 'red', 'Estados Unidos': 'blue', 'México': 'green'}

        # GRAFICO DE BARRAS
        sns.barplot(
            x='GENERO_ALUMNO',
            y='TOTAL',
            hue='CODIGO_DEPENDENCIA_ESTABLECIMIENTO',
            data=df_trabajar
        )

        # ASIGNAR CANTIDAD DE ALUMNOS A CADA BARRA
        for i in range(df_trabajar.shape[0]):
            bar = plt.gca().patches[i]
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height(), df_trabajar.loc[i, 'TOTAL'], ha="center", va="bottom", fontsize=8)

        
        # TITULOS Y ETIQUETAS
        plt.title(f'Cantidad de alumnos por genero y dependencia del establecimiento - {year}')
        plt.xlabel('Genero')
        plt.ylabel('Cantidad de alumnos')

        # MOVER LA LEYENDA FUERA DEL GRÁFICO Y AJUSTAR EL ESPACIO
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        # ALMACENAR GRAFICO
        plt.tight_layout()
        plt.savefig('Estadisticas/'+str(year)+'/Graficos/grafico_genero_dependencia'+str(year)+'.png')

        
    # Funcion para graficar promedio de alumnos por dependencia del establecimiento y genero
    def graficoPromedioDependencia(self, dataframe, year):
        df_trabajar = dataframe[[
            'PROMEDIO_GENERAL_ANUAL',
            'CODIGO_DEPENDENCIA_ESTABLECIMIENTO',
            'GENERO_ALUMNO'
            ]]

        # CAMBIAR REGISTROS POR MAPA DE DEPENDENCIA
        df_trabajar['CODIGO_DEPENDENCIA_ESTABLECIMIENTO'] = df_trabajar['CODIGO_DEPENDENCIA_ESTABLECIMIENTO'].map(self.map_dependencia)
        df_trabajar['GENERO_ALUMNO'] = df_trabajar['GENERO_ALUMNO'].map(self.map_genestu)

        # CONVERTIR PROMEDIO GENERAL A TIPO FLOAT
        df_trabajar['PROMEDIO_GENERAL_ANUAL'] = df_trabajar['PROMEDIO_GENERAL_ANUAL'].astype(float)

        # CALCULAR PROMEDIO DE PROMEDIO GENERAL DE ALUMNOS POR DEPENDENCIA Y GENERO
        df_trabajar = df_trabajar.groupby(['CODIGO_DEPENDENCIA_ESTABLECIMIENTO', 'GENERO_ALUMNO'])['PROMEDIO_GENERAL_ANUAL'].mean().reset_index()
        
        # GRAFICO DE BARRAS DE PROMEDIO DE PROMEDIO GENERAL DE ALUMNOS POR DEPENDENCIA Y GENERO
        plt.figure(figsize=(12, 8))
        sns.barplot(
            x='GENERO_ALUMNO', 
            y='PROMEDIO_GENERAL_ANUAL',
            hue='CODIGO_DEPENDENCIA_ESTABLECIMIENTO',
            data=df_trabajar
        )

        # ASIGNAR PROMEDIO DE PROMEDIO GENERAL A CADA BARRA
        for i in range(df_trabajar.shape[0]):
            bar = plt.gca().patches[i]
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height(), round(df_trabajar.loc[i, 'PROMEDIO_GENERAL_ANUAL'], 2), ha="center", va="bottom", fontsize=8)

        # ESTABLECER LIMITE EN Y EN 4
        plt.ylim(5, plt.ylim()[1])

        # CREAR LINEA PROMEDIO GENERAL Y SU VALOR ENCIMA DE LA LINEA A LA DERECHA DEL GRAFICO
        plt.axhline(df_trabajar['PROMEDIO_GENERAL_ANUAL'].mean(), color='black', linestyle='--', label='Promedio general')
        plt.text(1.1, df_trabajar['PROMEDIO_GENERAL_ANUAL'].mean(), round(df_trabajar['PROMEDIO_GENERAL_ANUAL'].mean(), 2), ha="center", va="bottom", fontsize=8)

        # TITULOS Y ETIQUETASestablecimientosunicos
        plt.title(f'Promedio de promedio general de alumnos por dependencia y genero - {year}')
        plt.xlabel('Dependencia')
        plt.ylabel('Promedio de promedio general')

        # MOVER LA LEYENDA FUERA DEL GRÁFICO Y AJUSTAR EL ESPACIO
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        # ALMACENAR GRAFICO
        plt.tight_layout()
        plt.savefig('Estadisticas/'+str(year)+'/Graficos/grafico_promedio_dependencia'+str(year)+'.png')

    # Funcion que obtenga los nombres de los establecimientos sin duplicados
    def getEstablecimientosUnicos(self, dataframe, year):
        try:
            rendimiento = dataframe
            df_establecimientos = rendimiento[['NOMBRE_ESTABLECIMIENTO', 'ROL_ESTABLECIMIENTO']].drop_duplicates()
            df_establecimientos.to_csv('Estadisticas/'+str(year)+'/establecimientos_unicos'+str(year)+'.csv', index=False)
            return df_establecimientos
        except Exception as e:
            print('Error al determinar los establecimientos unicos del año:', year)
            print('Error:', e)
            return None
