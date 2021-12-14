# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from movies.models import Actors, Movies

class ActorsView(View):
    def post(self, request):
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        date_of_birth = data['date_of_birth']
        movies = Movies.objects.get(title=data['movies'])
        if Actors.objects.filter(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth).exists():
            a = Actors.objects.get(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
            a.movies.add(movies)
            return JsonResponse({'message':'actor_movie updated'}, status=201)
        else:
            a = Actors.objects.create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
            a.save()
            a.movies.add(movies)
            return JsonResponse({'message':'created new actor'}, status=201)

    def get(self, request):
        actors = Actors.objects.all()
        actors_list = []
        for actor in actors:
            movies_titles = actor.movies.values_list('title')
            movies_list = []
            for m in movies_titles:
                movies_list.append(m[0])
            actors_list.append({'first_name':actor.first_name, 'last_name':actor.last_name, 'movies':movies_list})
        return JsonResponse({'results':actors_list}, status=200)

class MoviesView(View):
    def post(self, request):
        data = json.loads(request.body)
        title = data['title']
        release_date = data['release_date']
        running_time = data['running_time']
        Movies.objects.create(title=title, release_date=release_date, running_time=running_time)
        return JsonResponse({'message':'created new movie'}, status=201) 
    
    def get(self, request):
        movies = Movies.objects.all()
        movies_list = []
        for movie in movies:
            actors_querys = Actors.objects.filter(movies__title=movie.title).values_list('first_name')
            actors_list = []
            for actor in actors_querys:
                actors_list.append(actor[0])
            movies_list.append({'title':movie.title, 'running_time':movie.running_time, 'actor':actors_list})
        return JsonResponse({'results':movies_list}, status=200)