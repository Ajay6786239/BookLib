# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')  # Renamed from 'des' to 'description'
        if title and author and description:
            book = Book.objects.create(title=title, author=author, description=description)
            return JsonResponse({
                'success': True,
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'description': book.description  # Updated to match the field name
            })
        return JsonResponse({'success': False})

    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def delete_book(request, book_id):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return JsonResponse({'success': True})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Book not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
