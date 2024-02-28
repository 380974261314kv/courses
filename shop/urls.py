from django.urls import path
from shop import views

appname = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
]
