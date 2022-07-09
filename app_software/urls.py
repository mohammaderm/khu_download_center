from django.urls import path
from app_software.views import *

urlpatterns = [
    path('', home, name='home'),
    path('pagination/', Pagination_pro.as_view(), name='list'),
    path('software_detail/<str:slug>/', software2, name='software1'),
    path('mostlike/', mostlike, name='mostlike'),
    path('mostcomment/', mostcomment, name='mostcomment'),
    path('blogsoft_details/<str:slug>/', blogsoftdetails, name='blogsoftdetails'),
    path('blogs/', blogsoftpost, name='blogssoft'),
]
