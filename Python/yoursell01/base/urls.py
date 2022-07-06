from django.urls import path
from operator import concat
from .views import indexView, bundesligaView, premierlView, serieAView, menuView
urlpatterns = [
    path('', indexView.as_view()),
    path('', bundesligaView.as_view()),
    path('', premierlView.as_view()),
    path('', serieAView.as_view()),
    path('', menuView.as_view()),
]
