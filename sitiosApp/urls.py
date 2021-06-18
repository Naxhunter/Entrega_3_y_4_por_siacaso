from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',inicio, name='IND'),
    path('BASE', base, name='BASE'),
    path('SOLAYU', sol_ayu, name='SOLAYU'),
    path('MOTREC', mot_rec, name="MOTREC"),
<<<<<<< HEAD
    path('AYUDA',ayuda, name="AYUDA"),
=======
    path('LOGIN', login, name='LOGIN'),
>>>>>>> 718cdc46002d5a948bc8c2c71231f1f021b97f4e
]
