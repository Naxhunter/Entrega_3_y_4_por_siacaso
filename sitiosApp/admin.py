from django.contrib import admin
from .models import CategoriaUnormal,CategoriaUtrabajador,solicitudtrabajo,solicitudayuda

admin.site.register(CategoriaUtrabajador)
admin.site.register(CategoriaUnormal)
admin.site.register(solicitudtrabajo)
admin.site.register(solicitudayuda)
# Register your models here.
