from django.urls import path
from . import views


urlpatterns=[
    path('bcourse/', views.bcourse, name='bcourse'),
    path('battendance/', views.battendance, name='battendance'),
    path('bgrade/', views.bgrade, name='bgrade'),
    path('bactivity/', views.bactivity, name='bactivity'),
    
]