from django.urls import path
from . import views

urlpatterns = [
    path('pages/class1/theory.html', views.theory),
    path('pages/class1/code_test.html', views.code_test),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('',views.home),
]
