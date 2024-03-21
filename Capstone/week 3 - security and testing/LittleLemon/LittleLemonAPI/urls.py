from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message', views.msg),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('bookings', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
]

