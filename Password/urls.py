from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.button),
    path('generate',views.index,name='script'),
    path('qrcode',views.secureImage,name='code'),
    path('strength',views.strength,name='pass')
]
