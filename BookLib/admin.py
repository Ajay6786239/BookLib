from django.contrib import admin
from .models import Book

# Register your model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
