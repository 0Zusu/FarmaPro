from django.contrib import admin
from .models import Receta

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('Creacion','Estado')
admin.site.register(Receta,RecetaAdmin)