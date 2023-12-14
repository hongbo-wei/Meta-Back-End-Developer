from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view


# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})

    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        book = Book(
            title=title,
            author=author,
            price=price,
            inventory=inventory,
        )
        
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required filed missing'}, status=400)
        return JsonResponse(model_to_dict(book), status=201)
    
# For debut purpose
from django.http import HttpResponse
def display_even_numbers (request):
    response = ""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        remainder = i % 2
        if remainder == 0:
            response += str(i) + "<br/>"
    return HttpResponse (response)

# RESTful APIS
@api_view(['Get','POST'])
def book_list(request):
    return Response('list of the books', status=status.HTTP_200_OK)
