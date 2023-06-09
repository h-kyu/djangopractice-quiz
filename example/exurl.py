from django.urls import path
from . import views

app_name = 'example'

urlpatterns = [
    path('', views.index, name='index'),
    path('infoForm/', views.infoForm, name='infoForm'),
    path('infoResult/', views.infoResult, name='infoResult'),
    path('selectForm/', views.selectForm, name='selectForm'),
    path('selectResult/', views.selectResult, name='selectResult'),
    path('comboForm/', views.comboForm, name='comboForm'),
    path('forForm/', views.forForm, name='forForm'),
    path('forResult/', views.forResult, name='forResult'),
    path('lottoForm/', views.lottoForm, name='lottoForm'),
    path('lottoResult/', views.lottoResult, name='lottoResult'),
]