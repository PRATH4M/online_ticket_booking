# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('book/<int:event_id>/', views.book_ticket, name='book_ticket'),
]
