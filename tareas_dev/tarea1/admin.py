from django.contrib import admin
from .models import Station, Extra

class ExtrasInline(admin.TabularInline):
    """
    Clase para ingresar la informacion extra en la misma ventana de station
    """
    model = Extra
    extra = 1
    exclude=['uid']
        
class StationAdmin(admin.ModelAdmin):
    """
    Mejorando la vista en el administrador para visualizar la informacion
    """
    inlines = (ExtrasInline,)
    list_display=['name','empty_slots','free_bikes','timestamp']
    search_fields = ['name']
    list_filter = ['timestamp']
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()        
        for instance in instances:
            instance.save() 

admin.site.register(Station, StationAdmin)
# admin.site.register(Extra)