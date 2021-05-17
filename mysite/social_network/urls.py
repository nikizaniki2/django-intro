from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='sn-home'),
    path('about/', views.about, name='sn-about'),
]