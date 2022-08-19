from django.urls import path
from . import views


urlpatterns=[
    path('ocourse/', views.ocourse, name='ocourse'),
    path('oattendance/', views.oattendance, name='oattendance'),
    path('ograde/', views.ograde, name='ograde'),
    path('oactivity/', views.oactivity, name='oactivity'),
    
]