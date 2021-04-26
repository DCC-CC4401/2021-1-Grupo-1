from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.GetComunasView.as_view()),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('homepage/', views.HomepageView.as_view()),
    path('results/', views.ResultsView.as_view()),
]
