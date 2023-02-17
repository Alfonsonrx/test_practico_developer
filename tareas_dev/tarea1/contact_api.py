import requests

def get_data():
    """
    Se realiza una request a la API, esos datos se separan en stations y extras para luego pasarse a los modelos
    """
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago').json()
    
    stations = response['network']['stations']
    extras = []
    for station in stations:
        extras.append([station['id'], station['extra']])
        station.pop('extra')
    
    return stations, extras
