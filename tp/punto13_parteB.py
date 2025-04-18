# solicitar año, elegir el ultimo trimestre
# CH12 >= 7
# CONDICION_DE_HABITABILIDAD == Insuficiente
# AÑO = INPUT => TRIMESTRE == 4

from pathlib import Path
from funcion10 import condicion_de_habitabilidad as condi_hab
from dataset_indi_hoga import dataset_hogares as data_hog
from dataset_indi_hoga import dataset_individuals as data_indi
import json


zip_folder = Path('data_zip')

hog = data_hog(zip_folder)
condi_hab(hog)
indi = data_indi(zip_folder)

anio_usuario = input('Ingrese el año a buscar.')

hogares_insuficientes = {}

for hogar in hog:
    if hogar['ANO4'] == anio_usuario and hogar['TRIMESTRE'] == '4' and hogar['CONDICION_HABITABILIDAD'] == 'Insuficiente':
        clave = (hogar['CODUSU'], hogar['NRO_HOGAR'])
        hogares_insuficientes[clave] = True

contador = 0

for persona in indi:
    if persona['ANO4'] == anio_usuario and persona['TRIMESTRE'] == '4':
        clave = (persona['CODUSU'], persona['NRO_HOGAR'])
    if clave in hogares_insuficientes and persona['CH12'] >= 7:
        contador +=1

print(f"Cantidad de personas en viviendas con condición insuficiente y nivel universitario o superior: {contador}")
