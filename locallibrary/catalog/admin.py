from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)

class AuthorInstanceInline(admin.TabularInline):
	"""docstring for AuthorInstanceInline"""
	model = Book
		
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #order list columns
    inlines = [AuthorInstanceInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id', 'imprint') #display the titles of class
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
            'fields': ('book', 'imprint', 'id')
			}),
		('Availability', {
			'fields': ('status', 'due_back')
		}),
    )