from django.db.models import Q
from django.shortcuts import render
from credentialapp.models import Category,Movie

# Create your views here.

def search_result(request):
    query = None
    movies = None
    categories = None
    search_results=None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(title__icontains=query))

        categories = Movie.objects.filter(Q(category__name__icontains=query))

        search_results = list(movies) + list(categories)

    return render(request, 'search.html', {'movies': search_results, 'query': query})