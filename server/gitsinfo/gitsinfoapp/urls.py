from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('changeattr/', views.changeattr, name='changeattr'),
]
