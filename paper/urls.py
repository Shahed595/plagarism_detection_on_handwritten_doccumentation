from django.urls import path
from paper.views import home,store_paper,show_papers
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('store_paper/', store_paper, name='store_paper'),
    path('show_papers/', show_papers, name='show_papers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)