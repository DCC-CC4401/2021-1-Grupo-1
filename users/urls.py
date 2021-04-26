from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.GetComunasView.as_view()),
    path('base/', views.BaseView.as_view(), name='base'),
    path('base_authentication/', views.AuthenticationBaseView.as_view(), name='baseAuthentication'),

              ]
