from django.urls import path
from operator import concat
from .views import indexView, bundesligaView, premierlView, serieAView, menuView

urlpatterns = [
    path('', indexView.as_view(), name= 'index'),
    path('bundesliga/', bundesligaView.as_view(),name='bundesliga'),
    path('premierl/', premierlView.as_view(),name='premierl'),
    path('serieA/', serieAView.as_view(),name= 'serieA'),
    path('menu/', menuView.as_view(),name= 'menu'),
]
