from django.shortcuts import render
from .models import Movie 
from django.views.generic.base import View

class MoviesView(View):

	"""Список фильмов"""
	def get(self, request):
		movies = Movie.objects.all()
		context = {
			'movies' : movies 
		}
		return render(request, 'movies/movies.html', context)

