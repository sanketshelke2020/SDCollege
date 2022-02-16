from django.urls import path
from . import views
import dashboard

urlpatterns = [
    path('', views.register,name="register"),
    path('login', views.loginView, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logoutView, name="logout")

]
