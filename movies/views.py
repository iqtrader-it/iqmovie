from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    """Film`s list"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = 'movies/movies.html'

class MovieDetailView(DetailView):
    """Film1s details"""
    model = Movie
    slug_field = 'url'


