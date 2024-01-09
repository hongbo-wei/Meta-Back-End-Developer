from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
    path('numbers', views.display_even_numbers),
    path('book-list', views.book_list),
]