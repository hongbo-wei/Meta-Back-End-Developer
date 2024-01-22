from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from .models import *
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer
from .throttles import TenCallsPerMinute

# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MenuItemView(generics.ListCreateAPIView): #PUT, PATCH, DELETE
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category']
    search_fields = ['title', 'price']

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'DeliveryCrew', 'Manager']).exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def put(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def patch(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def delete(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView): #POST
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'DeliveryCrew', 'Manager']).exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def put(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def patch(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def delete(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message':'successful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute]) # UserRateThrottle
def throttle_check_auth(request):
    return Response({'message':'message for the logged in user only'})