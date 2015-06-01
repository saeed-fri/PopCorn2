from django.shortcuts import render
from Movie.models import Movie
import json
from django.http import HttpResponse

def search(request, query):
    movie_results = []
    user_results = []
    print(query)
    if query != '':
        movie_results = processQuery(query)
    return render(request, "search_results.html", {
        "movie_results": set(movie_results),
        })


def search_ajax(request):
    print("ok")
    query = request.GET['q']
    movie_results = {}
    # user_results = []
    if query != '':
        temp = processQueryJson(query)
        n = temp.__len__()
        # temp = serializers.serialize("json", temp)
        for i in range(0,n):
            # print(str(i) + temp[i].name)
            movie_results['t' + str(i)] = temp[i]
            # movie_results['t' + str(i)] = serializers.serialize("json", temp[i])
        print(movie_results)
        # movie_results = serializers.serialize("json", movie_results.get_queryset())
    return HttpResponse(json.dumps(movie_results), content_type="application/json")
    # return HttpResponse(movie_results, content_type="application/json")


def processQuery(query):
    movie_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        movie_results += Movie.objects.filter(name__contains=term)
    return movie_results


def processQueryJson(query):
    movie_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        movie_results += Movie.objects.filter(name__contains=term).values()
    return movie_results