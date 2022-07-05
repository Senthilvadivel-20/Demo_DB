from os import name
from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('player/<int:id>',views.generate_player_info,name='player info'),
    path('table',views.table,name='table'),
]

