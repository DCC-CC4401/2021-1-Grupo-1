from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post_view, name='post'),
]
