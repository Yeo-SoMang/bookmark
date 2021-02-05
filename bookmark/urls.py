from django.urls import path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', list, name='list'),
    path('new/', new, name='new'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
]