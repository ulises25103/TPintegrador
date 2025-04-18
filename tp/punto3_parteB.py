from dataset_indi_hoga import dataset_individuals as data_indi
from pathlib import Path

zip_folder = Path('data_zip')

indi = data_indi(zip_folder)

desocupacion = {}

for persona in indi:
    anio = persona['ANO4']
    trimestre = persona['TRIMESTRE']
    estado = persona['ESTADO']
    clave = (anio, trimestre)
    
    if clave not in desocupacion:
        desocupacion[clave] = {'desocupados': 0, 'total': 0}

    desocupacion[clave]['total'] += 1
    if estado == '2':
        desocupacion[clave]['desocupados'] += 1

resultados = []

for clave, valores in desocupacion.items():
    porcentaje = (valores['desocupados'] / valores['total']) * 100
    resultados.append({
        'año': clave[0],
        'trimestre': clave[1],
        'porcentaje_desocupacion': porcentaje
    })

resultado_min = min(resultados, key=lambda x: x['porcentaje_desocupacion'])

print(int(resultado_min['porcentaje_desocupacion']))