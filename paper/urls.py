from django.urls import path
from paper.views import home,store_paper,show_papers,edit_book,delete_paper
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('store_paper/', store_paper, name='store_paper'),
    path('show_papers/', show_papers, name='show_papers'),
    path('edit_book/<int:id>', edit_book, name='edit_book'),
    path('delete_paper/<int:id>', delete_paper, name='delete_paper')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)