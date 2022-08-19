from django.urls import path
from . import views


urlpatterns=[
    path('course/', views.course, name='course'),
    path('attendance/', views.attendance, name='attendance'),
    path('grade/', views.grade, name='grade'),
    path('activity/', views.activity, name='activity'),
    
]