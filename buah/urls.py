from  django.urls import path,include
from  buah.views import *
from  django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('dashboard', dashboard ,name='dashboard'), 
    path('tabel_buah', buahh ,name='tabel_buah'), 
    path('user', user,name='tabel_user'), 
    path('list', buah_list,name='buah_list'),
    path('add', buah_add,name='buah_add'),
    path('update/<int:id>', buah_update,name='buah_update'),
    path('delete/<int:id>', buah_delete,name='buah_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 