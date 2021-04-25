from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.GetComunas.as_view()),
    path('login/', views.LoginUserView.as_view(), name='login'),
]
