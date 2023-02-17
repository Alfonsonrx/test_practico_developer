from django.apps import AppConfig
from .contact_api import get_data

class Tarea1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tarea1'

    def ready(self): # Asegurando que la app esta encendida
        from .models import Station, Extra
        """
        Para asegurar que no se ingresaran datos repetidos se ejecutara solo si la base de datos esta vacia
        """
        if Station.objects.count()==0:
            stations, extras = get_data()
            for station in stations:
                Station.objects.create(
                    id=station['id'],
                    empty_slots=station['empty_slots'],
                    free_bikes=station['free_bikes'],
                    latitude=station['latitude'],
                    longitude=station['longitude'],
                    name=station['name'],
                    timestamp=station['timestamp'],
                )
            for extra in extras:
                station_id = extra[0]
                e = extra[1]
                
                Extra.objects.create(
                    uid = e['uid'],
                    station = Station.objects.get(pk = station_id),
                    address = e['address'],
                    altitude = e['altitude'],
                    ebikes = e['ebikes'],
                    has_ebikes = e['has_ebikes'],
                    last_updated = e['last_updated'],
                    normal_bikes = e['normal_bikes'],
                    payment = e['payment'],
                    payment_terminal = e['payment-terminal'],
                    post_code = e['post_code'] if e.get('post_code') is not None else "",
                    renting = e['renting'],
                    returning = e['returning'],
                    slots = e['slots'],
                )