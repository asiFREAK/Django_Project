from django.contrib import admin
from django.urls import path
from new_app import views as main_views

urlpatterns = [
    path('', main_views.main_index),
    path('mon/', main_views.main_mon, name='mon'),
    path('tues/', main_views.main_tues, name='tues'),
    path('wed/', main_views.main_wed, name='wed'),
    path('thur/', main_views.main_thur, name='thur'),
    path('fri/', main_views.main_fri, name='fri'),
    path('sat/', main_views.main_sat, name='sat'),
    path('sun/', main_views.main_sun, name='sun')
]
