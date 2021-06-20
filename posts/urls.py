from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.post_view, name='view_post'),
    path('create_post/', views.create_post_view, name='create_post'),
]
