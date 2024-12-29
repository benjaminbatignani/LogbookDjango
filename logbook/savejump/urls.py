from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.index, name='indexSaveJump'),
    path('saisie/', views.saisie, name='saisie'),
    path('jumpform/', views.jumpform, name='jumpform'),
    path('jumplist/', views.jumplist, name='jumplist'),
    path('login/', LoginView.as_view(next_page='/savejump/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/savejump/login/'), name='logout')
    ]