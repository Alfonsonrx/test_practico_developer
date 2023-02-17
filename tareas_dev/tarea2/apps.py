from django.apps import AppConfig
import json, os

class Tarea2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tarea2'

    def ready(self):
        from .models import Proyecto
        
        if Proyecto.objects.count()==0:
            proyectos_arr=json.load(open(os.path.join("archivos_json/",'datos_proyectos.json'),))['proyectos']
                
            for proyecto in proyectos_arr:
                
                Proyecto.objects.create(
                    id=proyecto['id'],
                    nombre=proyecto['nombre'],
                    tipo=proyecto['tipo'],
                    region=proyecto['region'],
                    tipologia=proyecto['tipologia'],
                    titular=proyecto['titular'],
                    inversion=proyecto['inversion'],
                    fecha_ingreso=proyecto['fecha_ingreso'],
                    estado=proyecto['estado'],
                )