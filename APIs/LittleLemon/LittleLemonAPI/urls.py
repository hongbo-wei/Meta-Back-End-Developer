from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view({'get':'list'})),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories', views.CategoriesView.as_view()),
    path('api-token-auth', obtain_auth_token), # obtain user token and test if its group have that permission
    path('groups/manager/users', views.managers),
    path('groups/manager/users/<int:userId>', views.ManagersDeleteView.as_view(), name='managers_delete'),
    path('groups/delivery-crew/users', views.delivery_crews),
    path('groups/delivery-crew/users/<int:userId>', views.DeliveryCrewsDeleteView.as_view(), name='delivery_crews_delete'),
    path('cart/menu-items', views.CartView.as_view({'get':'list'})),
    path('orders', views.OrdersView.as_view({'get':'list'})),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('throttle-check', views.throttle_check), # check anonymous Throttling
    path('throttle-check-auth', views.throttle_check_auth), # check user Throttling
]