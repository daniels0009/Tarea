"""
Ejercicio nivel 4: Rendimiento de cultivos en Colombia
Modulo de funciones.

@author: Cupi2
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#Parte 1
"""
Nombre de las columnas:
Departamento: Nombre del departamento productor.
• Municipio: Nombre del municipio productor.
• Tipo_Cultivo: Tipo de cultivo que se produce en el territorio.
• Cultivo: Cultivo específico que se produce en el territorio.
• Hectareas_sembradas: Cantidad de hectáreas sembradas en un cultivo en específico.
• Hectareas_cosechadas: Cantidad de hectáreas cosechadas en un cultivo en específico.
• Toneladas: Toneladas obtenidas al momento de cosechar un cultivo."""
#Requerimiento 0 - Cargar datos
"""def cargar_datos(archivo:str)-> pd.DataFrame:
    data = pd.read_csv(archivo)
    return data"""
def cargar_datos(path):
    data = pd.read_csv(path)
    return data
#Parte 2
#Requerimiento 1 - Distribución de tipos de cultivo en un departamento
"""agregar porcentajes al diagrama con el parametro: autopct='%.1f%%' """
def piechart_tipo_cultivo(dataframe: pd.DataFrame, departamento_seleccionado: str)-> None:
    toneladas_por_cultivo = obtener_toneladas_por_tipo_cultivo(dataframe, departamento_seleccionado)
    plt.pie(toneladas_por_cultivo, labels= toneladas_por_cultivo['Tipo_Cultivo'], autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title("Distribucion de toneladas por tipo de cultivo")
    plt.show()
    return None

#Requerimiento 2 - Top 10 cultivos toneladas cosechadas x hectárea
def diagrama_barras(dataFrame: pd.DataFrame)-> None:
    total_hectareas = dataFrame.groupby('Cultivo')['Hectareas_cosechadas'].sum().reset_index()
    total_toneladas = dataFrame.groupby('Cultivo')['Toneladas'].sum().reset_index()
    resultados = pd.merge(total_hectareas, total_toneladas, on='Cultivo', suffixes=('_hectareas', '_toneladas'))
    resultados['Metrica'] = resultados['Toneladas'] / resultados['Hectareas_cosechadas']

    nlargest = resultados.nlargest(10,'Metrica')

    plt.bar(nlargest['Cultivo'], nlargest['Metrica'])
    plt.xlabel('Cultivo')
    plt.ylabel('Toneladas por Hectárea')
    plt.title('Top 10 cultivos con mayor cantidad de toneladas cosechadas por hectarea')
    plt.show()

    return None

#Requerimiento 3 - Caja y bigotes de las toneladas producidas en los tipos de cultivos
def toneladas_tipo_cultivo(dataFrame: pd.DataFrame, departamento_seleccionado: str, rango_inicio: int, rango_final: int)->None:

    df_filtrado = filtrar_por_departamento(dataFrame,departamento_seleccionado) #me filtra por el departamento 
    df_filtrado.set_index('Tipo_Cultivo')
    print(obtener_toneladas_por_tipo_cultivo(dataFrame,departamento_seleccionado))

    df_filtrado = df_filtrado[(df_filtrado['Toneladas'] >= rango_inicio) & (df_filtrado['Toneladas'] <= rango_final)]

    print(df_filtrado)

    df_filtrado.boxplot(column='Toneladas', by='Tipo_Cultivo', figsize=(8,4))
    plt.xlabel('Tipo de Cultivo')
    plt.ylabel('Toneladas')
    plt.title("Toneladas producidas por tipo de cultivo")
    plt.show()
    
    return None

#Parte 3
#Requerimiento 4 - Construcción de la matriz de Departamento vs Tipo Cultivo
def crear_matriz(dataframe: pd.DataFrame) -> list:
  departments = sorted(dataframe["Departamento"].unique())
  departments_etiqueta = dict(enumerate(departments))
  
  tipos_cultivos = sorted(dataframe["Tipo_Cultivo"].unique())
  tipos_cultivos_etiqueta = dict(enumerate(tipos_cultivos))
  
  matriz = np.zeros((len(departments), len(tipos_cultivos)),dtype=int)  # Crea la matriz pero esta llena de ceros
  
  for i in range(len(departments)):
    for j in range(len(tipos_cultivos)):
      dept_x_cultivo = dataframe.loc[
        (dataframe['Departamento'] == departments[i]) & 
        (dataframe['Tipo_Cultivo'] == tipos_cultivos[j])
      ]
      
      matriz[i][j] = dept_x_cultivo['Hectareas_sembradas'].sum()
      
  return matriz, tipos_cultivos_etiqueta, departments_etiqueta


#Requerimiento 5 - Contar la cantidad total de toneladas producidas en un departamento dado
def obtener_toneladas_por_departamento_y_tipo_de_cultivo(department, crop_type, dataFrame):
    filtered_df = dataFrame[(dataFrame['Departamento'] == department) & (dataFrame['Tipo_Cultivo'] == crop_type)]
    total_toneladas = filtered_df['Toneladas'].sum()
    return total_toneladas

#Requerimiento 6 - Encontrar el departamento mayor o menor productor de un tipo de cultivo dado por el usuario
def depto_mayor_o_menor_productor (dataFrame: pd.DataFrame, mayor_menor:bool, Tipo_Cultivo:str)-> tuple:
    resultado = ()
    departamento = resultado[1]
    cantidad = resultado[2]
    if mayor_menor == "1":
        tipos_cultivo = dataFrame.items(['Tipo_cultivo',''])
        dataFrame.max()
        resultado.append()
        print('El departamento que es el', mayor_menor, 'productor de un tipo de cultivo en toneladas es', departamento, 'con', cantidad, 'toneladas')
    else:
        dataFrame.max(['Tipo_Cultivo','Departamento','Toneladas'])
        resultado.append()
        print('El departamento que es el', mayor_menor,'productor de un tipo de cultivo en toneladas es', departamento, 'con', cantidad, 'toneladas')

    return None

#Requerimiento 7 - Encontrar departamento productor estrella dado
def departamento_estrella(dataFrame:pd.DataFrame, tipo_cultivo:str, minimo_prod:int)->dict:
    depto_estrella_dict = {'Deptos':[],'Tipos':[]}


    x = 0
    return x
#Requerimiento 8 - : Mostrar producción por departamento
"""Importar matriz requerimiento 4 y organizar en una columna filtrada el tipo de cultivo que da el usuario

import matplotlib.image as mpimg
mapa = mpimg.imread("mapa.png").tolist()
plt.imshow(mapa)
plt.show()

def cargar_coordenadas(nombre_archivo:str)->dict:
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    titulos = archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()
    return deptos

"""#Codigos de colores:
#Rango        Valores RGB        Color
#0-10         0.94,0.10,0.10     Rojo
#10-100       0.94,0.10,0.85     Magenta
#100-1000     0.10,0.50,0.94     Azul
#1000-100000  0.34,0.94,0.10     Verde
#>=100000     0.99,0.82,0.09     Amarillo
"""
colores = {"0 a <10":[0.94, 0.10, 0.10], "10 a <100":[0.94, 0.10, 0.85], "100 a <1000":[0.10, 0.50, 0.94], "1000 a <100000":[0.34, 0.94, 0.10], ">=100000":[0.99, 0.82, 0.09]}
plt.imshow(mapa)
legends = []
for i in colores:
        legends.append(mpatches.Patch(color = colores[i], label=i))
        plt.legend(handles = legends, loc = 3, fontsize='x-small')
        plt.title("Producción en toneladas de " + tipo_cultivo, fontsize='x-small')
        plt.show()
    """
#___________________________________________________
def filtrar_por_departamento(dataFrame: pd.DataFrame, municipio_seleccionado: str)-> pd.DataFrame:
    if municipio_seleccionado in dataFrame['Departamento'].values:
        df_municipio = dataFrame[dataFrame['Departamento'] == municipio_seleccionado] #solo las que sean iguales al municipio seleccionado
        return df_municipio
    else:
        print(f"El municipio {municipio_seleccionado} no está en el DataFrame. Intentelo de nuevo")
    return None

def obtener_toneladas_por_tipo_cultivo(dataFrame,municipio_seleccionado):
    return filtrar_por_departamento(dataFrame,municipio_seleccionado).groupby('Tipo_Cultivo')['Toneladas'].sum().reset_index()



def cantidad_toneladas_departamento(matriz: tuple, departamento:str):
    matrix = matriz[0]
    dict_cultivos = matriz[1] 
    dict_depart = matriz[2]
    
    return None