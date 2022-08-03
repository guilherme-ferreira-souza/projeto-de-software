from django.urls import path
from operator import concat
from .views import indexView, bundesligaView, premierlView, serieAView, menuView

urlpatterns = [
    path('index/', indexView.as_view()),
    path('bundesliga/', bundesligaView.as_view()),
    path('premierl/', premierlView.as_view()),
    path('serieA/', serieAView.as_view()),
    path('menu/', menuView.as_view()),
]
