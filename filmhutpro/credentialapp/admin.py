from django.contrib import admin
from .models import Category, Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release_date','user')
    list_filter = ('category', 'release_date')
    search_fields = ('title', 'category', 'actors')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
