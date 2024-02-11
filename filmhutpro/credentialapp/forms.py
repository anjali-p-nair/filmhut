from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MovieForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        movie = super(MovieForm, self).save(commit=False)
        if self.user:
            movie.user = self.user
        if commit:
            movie.save()
        return movie
