from django.urls import path
from . import views

app_name = 'searchapp'
urlpatterns = [
    path('', views.search_result, name='search_Result'),
    ]
