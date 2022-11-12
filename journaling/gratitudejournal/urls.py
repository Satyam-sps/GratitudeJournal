from django.urls import path
from .views import CreateJournal,Index,DeleteJournal,UpdateJournal, DetailJournal


from django.conf import settings
from django.conf.urls.static import static

app_name = 'gratitudejournal'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('create',CreateJournal.as_view(),name='create'),
    path('delete/<int:pk>',DeleteJournal.as_view(),name='delete'),
    path('update/<int:pk>',UpdateJournal.as_view(),name='update'),
    path('detail/<int:pk>',DetailJournal.as_view(), name='detail'),
    # path('lifelog_create', CreateLifeLog.as_view() , name='create-lifelog'),
   
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    