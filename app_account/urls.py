from django.conf.urls import url
from app_account.views import signup, Profile, bookmarksdisplay, softrequest, booksend
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('profile/', Profile, name='dashboard'),
    path('bookmarks/', bookmarksdisplay, name='bookmark'),
    path('softrequest/', softrequest, name='softrequests'),
    path('sends/', booksend, name='booksend'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
