from django.contrib import admin
from .models import carrera,aula,profesor,materia, reserva_aula, horario_materia
# Register your models here.
admin.site.register(carrera)
admin.site.register(aula)
admin.site.register(profesor)
admin.site.register(materia)
admin.site.register(reserva_aula)
admin.site.register(horario_materia)