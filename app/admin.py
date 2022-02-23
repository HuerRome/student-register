from django.contrib import admin

from app.models import *

# Register your models here.
#Registrar los modelos para poder administrarlos
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)




