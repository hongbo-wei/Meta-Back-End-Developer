from django.shortcuts import render
# recap: user authentication
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

# Create your views here.
class MenuItemsView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return JsonResponse({"message":"This view is protected"})


# add the registration page
# http://127.0.0.1:8000/auth/users/

# Excersice: Securing the table booking
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer