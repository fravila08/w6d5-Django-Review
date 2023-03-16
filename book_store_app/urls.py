from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books),
    path('book/<int:id>/', views.book_info),
    path('books/', views.all_books)
]
