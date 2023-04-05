from django.urls import path
from . import views # . : 같은 패키지의 views를 가져옴

urlpatterns = [
    path('handsome/', views.handsome),
    path('index/', views.index),
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read)
]