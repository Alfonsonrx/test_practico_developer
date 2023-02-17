from django.contrib import admin
from .models import Proyecto

class ProyectoAdmin(admin.ModelAdmin):
    list_display=['nombre','fecha_ingreso','millones_inversion_usd','estado']
    search_fields = ['nombre']
    list_filter = ['fecha_ingreso']
    
admin.site.register(Proyecto, ProyectoAdmin)