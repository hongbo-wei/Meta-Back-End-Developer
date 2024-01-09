from django.urls import path 
from . import views 

# path('home/', views.home),
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name='getform'),
    path('booking/', views.form_view),
    
    path('home/', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'), 

    path('about/', views.about, name='about')

] 