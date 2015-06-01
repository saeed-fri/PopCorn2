from django.http import Http404
from django.shortcuts import render
from .models import Movie, Cast, Crew


def movie(request,movie_id):
    movie_o = Movie.objects.filter(id=movie_id)
    if movie_o.__len__() > 0:
        movie_o = movie_o[0]
    else:
        raise Http404("Movie does not exist")
    casts = Cast.objects.filter(movie_id=movie_id)
    crews = Crew.objects.filter(movie_id=movie_id)
    rating = movie_o.rating_sum * 2
    if movie_o.rating_count != 0:
        rating //= movie_o.rating_count
        rating /= 2
    else:
        rating = '-'
    return render(request, "movie_profile.html", {
        'movie': movie_o,
        'image_address': 'img/posters/' + str(movie_o.id) + '.jpg',
        'rating': rating,
        'casts': casts,
        'crews': crews,
        })