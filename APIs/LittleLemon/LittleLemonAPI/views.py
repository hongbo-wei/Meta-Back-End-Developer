from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .throttles import TenCallsPerMinute

# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemView(viewsets.ModelViewSet):
# class MenuItemView(generics.ListCreateAPIView): #PUT, PATCH, DELETE
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # Conditional throttling -> https://www.coursera.org/learn/apis/supplement/1h6WO/api-throttling-for-class-based-views

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    ordering_fields = ['price', 'category']
    filterset_fields = ['price', 'category']
    search_fields = ['title', 'price']

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'Delivery Crew', 'Manager','']).exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Created"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def put(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def patch(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def delete(self, request):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView): #POST
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    # Set the permission classes for the view
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'Delivery Crew', 'Manager', '']).exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Created"}, status=201)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def put(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def patch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)

    def delete(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            return Response({"message": "Authorized"}, status=200)
        else:
            return Response({"message": "Unauthorized"}, status=403)


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET', 'POST', 'DELETe'])
@permission_classes([IsAuthenticated])
def managers(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Authorized"}, status=200)
            # username = request.data['username']
        # if username:
        #     user = get_object_or_404(User, username=username)
        #     managers = Group.objects.get(name="Manager")
        #     if request.method == 'POST':
        #         managers.user_set.add(user)
        #     elif request.method == 'DELETE':
        #         managers.user_set.remove(user)
        #     return Response({"message": "OK"})
        return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"message": "Unauthorized"}, status=403)

class ManagerUsersView(APIView):
    def get(self, request):
        if request.user.groups.filter(name='Manager').exists():
            # Assuming the 'Manager' group exists
            manager_group = Group.objects.get(name='Manager')

            # Retrieve users belonging to the 'Manager' group
            manager_users = User.objects.filter(groups=manager_group)

            # Serialize the data
            serializer = UserSerializer(manager_users, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "Unauthorized"}, status=403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message':'successful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute]) # UserRateThrottle
def throttle_check_auth(request):
    return Response({'message':'message for the logged in user only'})