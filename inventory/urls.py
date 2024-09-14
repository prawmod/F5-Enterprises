from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.register, name='login'),
    path('logout/', views.logout_view, name='logout'),

]

