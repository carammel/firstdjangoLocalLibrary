from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    #paginate_by = 10 #if books are too much, page by page
    #context_object_name = 'my_book_list'   # your own name for the list as a template variable

    def get_queryset(self):
        return Book.objects.order_by('-title')
        #return Book.objects.filter(title__icontains='e')[:5] # Get 5 books containing the title war

    template_name = 'books/books_list.html'  # Specify your own template name/location 
    # if multiple views use same model we should create more template
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name2 = 'books/book_detail.html'
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        
        return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.order_by('-first_name')

    template_name3 = 'authors/author_list.html'  # Specify your own template name/location 
    # if multiple views use same model we should create more template
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name4 = 'authors/author_detail.html'
    def author_detail_view(request, primary_key):
        try:
            book = Author.objects.get(pk=primary_key)
        except Author.DoesNotExist:
            raise Http404('Author does not exist')
        
        return render(request, 'catalog/author_detail.html', context={'Author': Author})