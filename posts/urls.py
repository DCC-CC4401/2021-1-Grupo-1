from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_view, name='post'),
    #path('post/<int:post_id>', views.post_view, name='post'),
]
