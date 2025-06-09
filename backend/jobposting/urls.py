from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_jobposting),
    path('add/', views.add_jobposting),
    path('details/<int:id>/', views.job_details),
]
