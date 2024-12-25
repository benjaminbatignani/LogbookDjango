from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='indexSaveJump'),
    path('saisie/', views.saisie, name='saisie'),
    path('jumpform/', views.jumpform, name='jumpform'),
    ]