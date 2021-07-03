from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>', views.post_view, name='post_view'),
    path('create_post/', views.create_post_view, name='create_post'),
    path('api/interested/<int:user_id>/<int:post_id>', views.interested_api, name='interested_api')
]
