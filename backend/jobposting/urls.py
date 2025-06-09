from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_jobposting),
    path('add/', views.add_jobposting),
]
