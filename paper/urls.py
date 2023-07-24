from django.urls import path
from paper.views import home,store_paper
urlpatterns = [
    path('', home, name='home'),
    path('store_paper/', store_paper, name='store_paper')
]