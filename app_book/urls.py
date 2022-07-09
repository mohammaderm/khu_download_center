from django.urls import path
from app_book.views import *

urlpatterns = [
    path('books/', bookhome, name='bookhome'),
    path('book-pagination/', Pagination.as_view(), name='pagination'),
    path('mostlike-book/', Mostlike.as_view(), name='mostlikes'),
    path('mostcom-book/', Mostcom.as_view(), name='mostcoms'),
    path('stores/', Store.as_view(), name='stores'),
    path('storesf/', Storef.as_view(), name='storesf'),
    path('booksugest/', bookpost, name='bookpost'),
    path('book_detail/<str:slug>/', bookdetails, name='bookdetails'),
    path('blogbook_details/<str:slug>/', blogbookdetails, name='blogdetails'),
    path('blog/', blogpost, name='blogs'),
]
