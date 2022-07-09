from django.urls import path
from app_api.views import like, bookmark, cumment, cummentdisplay
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('like/', like, name='like'),
    path('bookmark/', bookmark, name='bookmark'),
    path('cumment/', cumment, name='cumment'),
    path('token/', auth_view.obtain_auth_token),
    path('cumment-display/', cummentdisplay, name='cumment_display'),
]
