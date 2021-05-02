from django.urls import path
from . import views

urlpatterns = [
    path('api/get_comunas/<int:region_id>', views.get_comunas_view),
    path('login/', views.login_user_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
    path('profile/edit/<int:user_id>', views.ProfileEditView.as_view(), name='profile_edit'),
]
