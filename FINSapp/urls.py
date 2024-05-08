from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.process_fins, name='process-fins'),
    path('result/', views.process_fins, name='process-fins'),
]