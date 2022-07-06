from django.urls import path
from operator import concat
from .views import indexView
urlpatterns = [
    path('', indexView.as_view()),
]
