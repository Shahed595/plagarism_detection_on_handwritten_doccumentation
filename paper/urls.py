from django.urls import path
from paper.views import home
urlpatterns = [
    path('', home, name='home')
]