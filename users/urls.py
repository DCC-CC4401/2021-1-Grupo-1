from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.get_comunas_view),
    path('login/', views.login_user_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('view_profile/', views.profile_view, name='view_profile'),
    path('config_profile/', views.profile_config, name='config_profile'),
]
