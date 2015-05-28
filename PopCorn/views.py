from django.shortcuts import render
from Movie.models import Movie


def search(request, query):
    movie_results = []
    user_results = []
    if query != '':
        terms = query.split('/')
        print(terms)
        # terms = [term.strip() for term in query.split()]
        for term in terms:
            movie_results += Movie.objects.filter(name__contains=term)
            # movie_results.append(Q(content__icontains=term))
    return render(request, "search_results.html", {
        "movie_results": movie_results,
        })