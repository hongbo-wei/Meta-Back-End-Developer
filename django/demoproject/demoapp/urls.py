from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('home/', views.home),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path('booking/', views.form_view),
] 