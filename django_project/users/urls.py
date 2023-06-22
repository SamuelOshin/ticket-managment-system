from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_staff, name='register_staff'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
]
