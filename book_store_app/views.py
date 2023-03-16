from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def all_books(request):
    if request.method == 'GET':
        data ={
            "books" : Book.objects.all().values(),
            "authors" : Author.objects.all().values()
        }
        return render(request, "pages/books.html", data)
    
    elif request.method == 'POST':
        body = json.loads(request.body)
        author = Author.objects.all().get(first_name = body['first'], last_name = body['last'])
        new_book = Book.objects.create(title = body['title'], description = body['description'], price = body['price'], author = author)
        new_book.save()
        return JsonResponse({'success': True})
    
    
@csrf_exempt
def book_info(request, id):
    book = Book.objects.all().get(id = id)
    author = book.author
    if request.method == 'GET':
        data = {
            "book" : book,
            "author": book.author
        }
        return render(request, "pages/book.html", data)
    
    elif request.method == 'PUT':
        body = json.loads(request.body)
        book.title = body['title']
        book.description = body['description']
        book.price = body['price']
        author.first_name = body['first_name']
        author.last_name = body['last_name']
        author.save()
        book.save()
        return JsonResponse({'success':True})
    
    elif request.method == 'DELETE':
        book.delete()
        return JsonResponse({'success':True})