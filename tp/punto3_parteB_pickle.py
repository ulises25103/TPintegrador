from dataset_indi_hoga import dataset_individuals as data_indi
from pathlib import Path
import pickle

zip_folder = Path('data_zip')
pkl_path = Path('individuos.pkl')

if pkl_path.exists():
    # Cargar desde el archivo ya guardado
    with open(pkl_path, 'rb') as f:
        indi = pickle.load(f)
    print('Datos cargados desde Pickle ✅')
else:
    # Procesar los ZIPs y guardar en Pickle
    indi = data_indi(zip_folder)
    with open(pkl_path, 'wb') as f:
        pickle.dump(indi, f)
    print('Datos procesados y guardados en Pickle ✅')

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