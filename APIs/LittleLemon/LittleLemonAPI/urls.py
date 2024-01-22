from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category', views.CategoriesView.as_view()),
    path('api-token-auth', obtain_auth_token), # obtain user token and test if its group have that permission
    path('throttle-check', views.throttle_check), # check anonymous Throttling
    path('throttle-check-auth', views.throttle_check_auth), # check user Throttling
]