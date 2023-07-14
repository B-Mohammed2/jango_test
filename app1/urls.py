from django.urls import path
from . import views

urlpatterns=[ path('app1_function/', views.app1_function, name='app1_function'),]