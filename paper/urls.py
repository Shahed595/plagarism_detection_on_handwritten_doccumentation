from django.urls import path
from paper.views import home,store_paper,show_papers
urlpatterns = [
    path('', home, name='home'),
    path('store_paper/', store_paper, name='store_paper'),
    path('show_papers/', show_papers, name='show_papers'),
]