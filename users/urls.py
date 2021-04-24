from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.GetComunas.as_view()),
    #path('base', views.base, name='base_comun'),
]
