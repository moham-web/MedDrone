from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login, name="login"), 
    path('', views.home , name="home"),
    path('Manager/', views.manager_view, name="manager"),  
    path('Employe/', views.employe_view, name="employe"),  
    path('logout/', views.logout_view, name='logout'),  # Define URL for logout

]