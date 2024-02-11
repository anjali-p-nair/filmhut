from . import views
from django.urls import path
app_name='filmapp'


urlpatterns = [
    path('',views.index ,name='index'),
    path('movie_detail/<int:movie_id>/',views.movie_detail,name='movie_detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('view_profile/',views.view_profile,name='view_profile'),
    ]