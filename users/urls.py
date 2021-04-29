from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.get_comunas_view),
    path('login/', views.login_user_view, name='login'),
    path('homepage/', views.HomepageView.as_view()),
    path('results/', views.ResultsView.as_view()),
    path('register/', views.register_view, name='register'),
]
