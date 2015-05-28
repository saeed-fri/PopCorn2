from django.shortcuts import render
from .models import Movie, Cast, Crew


def movie(request,movie_id):
    movie_o = Movie.objects.filter(id=movie_id)[0]
    casts = Cast.objects.filter(movie_id=movie_id)
    crews = Crew.objects.filter(movie_id=movie_id)
    rating = movie_o.rating_sum
    if movie_o.rating_count != 0:
        rating /= movie_o.rating_count
    else:
        rating = '-'
    return render(request, "movie_profile.html", {
        'movie': movie_o,
        'image_address': 'img/posters/' + str(movie_o.id) + '.jpg',
        'rating': rating,
        'casts': casts,
        'crews': crews,
        })