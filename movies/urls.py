from django.urls import path
from .views import home, cinema
urlpatterns = [
    path('', home),
    path('cinema/', cinema, name='cinema')
]
