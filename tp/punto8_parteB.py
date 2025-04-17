#  REGION
#  II7 == 03
# crear un diccionario con cada region como key, cada valor es su porcentaje de inquilinos
from pathlib import Path
from dataset_indi_hoga import dataset_hogares as data_hog


zip_folder = Path('data_zip')
hogares = data_hog(zip_folder)


region_totales = {}

for hogar in hogares:
    region = hogar['REGION']
    inqui = hogar['II7']
    clave = region

    if not clave in region_totales:
        region_totales[clave] = {'inquilinos': 0, 'total': 0}
    
    region_totales[clave]['total'] += 1
    if hogar[inqui] == '03':
        region_totales[clave]['inquilino'] += 1

region_porcentaje = []

for clave, valor in region_totales.items():
    porcentaje = (valor['inquilinos'] / valor['total'] * 100)
    region_porcentaje.append({
        'region': clave,
        'porcentaje_inquilinos': porcentaje
    })

region_porcentaje.sort(reverse = True)

print(region_porcentaje)