from django.urls import path
from . import views

urlpatterns = [

    path('login', views.login),
    path('logout', views.logout),
    path('duplication_check',views.duplication_check),
    path('signUp',views.signUp),

    path('judge',views.judge),
    path('quiz',views.quiz),

    path('', views.index),
    path('pages/profile', views.profile),
    path('pages/signUp', views.signUp),

    path('classes/main/homepage', views.home),
    path('classes/main/class_start', views.class_start),    
    path('classes/step<int:page>/<str:name>', views.step),    

]
