from django.contrib import admin
from .models import carrera,aula,profesor,materia
# Register your models here.
admin.site.register(carrera)
admin.site.register(aula)
admin.site.register(profesor)
admin.site.register(materia)
