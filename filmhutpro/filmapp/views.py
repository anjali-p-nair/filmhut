from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from credentialapp.models import Movie
from credentialapp.forms import MovieForm
from .forms import UserProfileForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6)  # Display 6 movies per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'movies': movies,'page_obj':page_obj})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

#Update movie

def update(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Please log in to update a movie.')
        return redirect('credentialapp:login')

    movie = get_object_or_404(Movie, id=id)

    # Check if the logged-in user is the owner of the movie
    if movie.user != request.user:
        messages.info(request, 'You cannot update this movie.')
        return redirect('filmapp:movie_detail',movie_id=id)

    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        messages.success(request, 'Movie updated successfully.')
        return redirect('filmapp:movie_detail',movie_id=id)

    return render(request, 'update.html', {'form': form, 'movie': movie})


#delete function

def delete(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Please log in to delete a movie.')
        return redirect('credentialapp:login')

    movie = get_object_or_404(Movie, id=id)

    # Check if the logged-in user is the owner of the movie
    if movie.user != request.user:
        messages.info(request, 'You cannot delete this movie.')
        return redirect('filmapp:movie_detail',movie_id=id)

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully.')
        return redirect('filmapp:index')

    return render(request, 'delete.html', {'movie': movie})


#profile function

@login_required
def view_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('filmapp:view_profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form})