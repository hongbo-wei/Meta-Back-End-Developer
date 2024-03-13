from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import JsonResponse  # Import JsonResponse
from django.utils import timezone
from rest_framework import generics, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer, UserSerializer
from .throttles import TenCallsPerMinute

# Create your views here.
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['title']


# Menu-items endpoints
# menu-items
class MenuItemsView(viewsets.ModelViewSet):
# class MenuItemsView(generics.ListCreateAPIView): #PUT, PATCH, DELETE
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # Conditional throttling -> https://www.coursera.org/learn/apis/supplement/1h6WO/api-throttling-for-class-based-views

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    # filter, sorting, and searching
    filterset_fields = ['price', 'category']
    ordering_fields = ['price', 'category']
    search_fields = ['category__title', 'title', 'price']

    # Set the permission classes for the view
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'Delivery Crew', 'Manager','']).exists():
            return Response({"message": "Authorized"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        if request.user.groups.filter(name='Manager').exists():
            title = request.data.get('title')
            price = request.data.get('price')
            feature = request.data.get('feature')
            category_id = request.data.get('category')
            try:
                category = Category.objects.get(id=category_id)
                MenuItem.objects.create(title=title, price=price, feature=feature, category=category)
                return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
            except Category.DoesNotExist:
                return Response({"message": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


# menu-items/{menuItem}
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView): #POST
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = MenuItemSerializer

    # Set the permission classes for the view
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()

    def get(self, request, pk):
        # Check if the user is a customer or delivery crew
        if request.user.groups.filter(name__in=['Customer', 'Delivery Crew', 'Manager', '']).exists():
            cart_items = MenuItem.objects.filter(id=pk)
            serializer = MenuItemSerializer(cart_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.groups.filter(name='Manager').exists():
            title = request.data.get('title')
            price = request.data.get('price')
            feature = request.data.get('feature')
            if title is not None:
                menu_item.title = title
            if price is not None:
                menu_item.price = price
            if feature is not None:
                menu_item.feature = feature
            menu_item.save()
            return Response({"message": "Authorized and Updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.groups.filter(name='Manager').exists():
            title = request.data.get('title')
            price = request.data.get('price')
            feature = request.data.get('feature')
            if title is not None:
                menu_item.title = title
            if price is not None:
                menu_item.price = price
            if feature is not None:
                menu_item.feature = feature
            menu_item.save()
            return Response({"message": "Authorized and Updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            menu_item = MenuItem.objects.get(pk=pk)
            menu_item.delete()
            return Response({"message": "Authorized and Deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


# User group management endpoints
# Manager group
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def managers(request):
    managers_group = Group.objects.get(name="Manager")

    if request.user.groups.filter(name='Manager').exists() and request.method == 'GET':
        manager_users = User.objects.filter(groups=managers_group)
        serializer = UserSerializer(manager_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.user.groups.filter(name='Manager').exists() and request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        managers_group.user_set.add(user)
        return Response({"message": "OK"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    
class ManagersDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, userId):
        user = get_object_or_404(User, id=userId)
        managers_group = Group.objects.get(name="Manager")
        if request.user.groups.filter(name='Manager').exists():
            managers_group.user_set.remove(user)
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)


# Delivery Crew group
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def delivery_crews(request):
    delivery_crews_group = Group.objects.get(name="Deliver Crew")

    if request.user.groups.filter(name='Manager').exists() and request.method == 'GET':
        delivery_crews_users = User.objects.filter(groups=delivery_crews_group)
        serializer = UserSerializer(delivery_crews_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.user.groups.filter(name='Manager').exists() and request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        delivery_crews_group.user_set.add(user)
        return Response({"message": "OK"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    

class DeliveryCrewsDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, userId):
        user = get_object_or_404(User, id=userId)
        delivery_crews_group = Group.objects.get(name="Deliver Crew")
        if request.user.groups.filter(name='Manager').exists():
            delivery_crews_group.user_set.remove(user)
            return Response({"message": "Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    

# Cart management endpoints
class CartView(viewsets.ModelViewSet):
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = CartSerializer

    # Set the permission classes for the view
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # override default behavior of Django REST framework
    # viewsets when using ModelViewSet
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Manager').exists():
                return Cart.objects.all()
            elif user.groups.filter(name='Customer').exists():
                return Cart.objects.filter(user=user)
        return Cart.objects.none()

    def get(self, request):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user = self.request.user
        if not user.groups.filter(name__in=['Customer', 'Manager']).exists():
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request):
        # serializer for the post form
        user = self.request.user
        if user.groups.filter(name__in=['Customer', 'Manager']).exists():
            # Calculate total price
            total_price = int(request.data['quantity']) * float(request.data['unit_price'])
            menuitem = MenuItem.objects.get(id=request.data['menuitem'])
            # unit_price = MenuItem.objects.get(pk=menuitem).price
            # total_price = int(request.data['quantity']) * unit_price)
            new_cart = Cart.objects.create(user=request.user,
                                           menuitem=menuitem,
                                           quantity=request.data['quantity'],
                                           unit_price=request.data['unit_price'],
                                           price=total_price)
            # Save the cart item to the database
            serializer = CartSerializer(new_cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        user = self.request.user
        if user.groups.filter(name='Customer').exists():
            cart_items = Cart.objects.filter(user=user)
            cart_items.delete()
            return Response({"message": "Cart Cleared"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)


# Order management endpoints
class OrdersView(viewsets.ModelViewSet):
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    # filter, sorting, and searching
    filterset_fields = ['user', 'status']
    ordering_fields = ['user', 'status', 'total', 'date']
    search_fields = ['user', 'status', 'date']

    # Set the permission classes for the view
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        if user:
            if user.groups.filter(name='Customer').exists():
                orders = Order.objects.filter(user=user)
                return orders
            elif user.groups.filter(name='Manager').exists():
                orders = Order.objects.all()
                return orders
            elif user.groups.filter(name='Delivery Crew').exists():
                orders = Order.objects.filter(delivery_crew=user)
                return orders   
            else:
                return Response({"message": "Unauthorized"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request):
        user = request.user
        if user.groups.filter(name='Customer').exists():
            try:
                # Get current cart items for the current user (Assuming you have a Cart model)
                cart_items = Cart.objects.filter(user=request.user)
                if cart_items.exists():
                    # Calculate total price of the order
                    total_price = sum(item.price for item in cart_items)
                    # Check for the current date
                    current_date = timezone.now().date()
                    new_order = Order.objects.create(user=request.user, total=total_price, date=current_date)
                    for cart_item in cart_items:
                        order_item = OrderItem.objects.create(
                            order=new_order,
                            menuitem=cart_item.menuitem,
                            quantity=cart_item.quantity,
                            unit_price=cart_item.unit_price,
                            price=cart_item.price,
                        )

                    # Delete all items from the cart for this user
                    cart_items.delete()
                    # Serialize the newly created order and return it in the response
                    serializer = OrderSerializer(new_order)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "No items found in the cart."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN) # 403_FORBIDDEN



class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    #throttling control
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # filter, sorting, and searching
    filterset_fields = ['menuitem', 'order']
    ordering_fields = ['menuitem', 'order', 'quantity', 'unit_price', 'price']
    search_fields = ['menuitem', 'order']

    # Set the permission classes for the view
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self, request, pk):
        try:
            # Retrieve the order associated with the provided orderId
            # when we use .first() on a QuerySet in Django
            # the result from a collection of objects (the QuerySet) to a single object
            order = Order.objects.filter(pk=pk).first()
            # Check if the order belongs to the current user
            if order.user == request.user:
                # Retrieve all items for the order
                order_items = OrderItem.objects.filter(order_id=pk)
                serializer = OrderItemSerializer(order_items, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'This order does not belong to the current user.'}, status=status.HTTP_403_FORBIDDEN)

        except Order.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Update all attributes, send entire resource representation
    # including all fields, not just the fields you want to update
    def put(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            try:
                order = Order.objects.filter(pk=pk).first()
            except Order.DoesNotExist:
                return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
            
            # Update order status and delivery crew if provided in request data
            delivery_status = request.data.get('status')
            delivery_crew = request.data.get('delivery_crew')
            if delivery_status is not None:
                order.status = delivery_status
            if delivery_crew is not None:
                delivery_crew = get_object_or_404(User, id=delivery_crew)
                order.delivery_crew = delivery_crew
            order.save()
            return Response({"message": "Delivery updated successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    # Partially update one or more attributes
    def patch(self, request, pk):
        user = request.user
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        if request.user.groups.filter(name='Manager').exists():
            # Update order status and delivery crew if provided in request data
            delivery_status = request.data.get('status')
            delivery_crew = request.data.get('delivery_crew')
            if delivery_status is not None:
                order.status = delivery_status
            if delivery_crew is not None:
                delivery_crew = get_object_or_404(User, id=delivery_crew)
                order.delivery_crew = delivery_crew
            order.save()
            return Response({"message": "Delivery updated successfully"}, status=status.HTTP_200_OK)
            
        elif request.user.groups.filter(name='Deliver Crew').exists():
            if order.delivery_crew == user:
                # Update order status and delivery crew if provided in request data
                delivery_status = request.data.get('status')
                if delivery_status is not None:
                    order.status = delivery_status
                order.save()
                return Response({"message": "Delivery status updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Delivery crew id doesn't match"}, status=status.HTTP_403_FORBIDDEN)
            
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.groups.filter(name='Manager').exists():
            order_items = OrderItem.objects.filter(order=pk)
            order_items.delete()
            return Response({"message": "Authorized and Deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

# Throttling
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message':'successful'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute]) # UserRateThrottle
def throttle_check_auth(request):
    return Response({'message':'message for the logged in user only'})