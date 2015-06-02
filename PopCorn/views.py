from django.shortcuts import render
from Movie.models import Movie
from User.models import UserProfile
import json
from django.http import HttpResponse
import datetime


def search(request, query):
    now = datetime.datetime.now()
    movie_results = []
    user_results = []
    print(query)
    if query != '':
        movie_results = processQuery(query)
        user_results = processQueryUsers(query)
    return render(request, "search_results.html", {
        "movie_results": set(movie_results),
        "user_results": set(user_results),
        "year": -1 * now.year
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


def processQueryUsers(query):
    user_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        user_results += UserProfile.objects.filter(alias__contains=term)
    return user_results


def processQueryUsersJson(query):
    users_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        users_results += UserProfile.objects.filter(alias__contains=term).values()
    return users_results


def processQuery(query):
    movie_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        movie_results += Movie.objects.filter(name__contains=term)
        movie_results += Movie.objects.filter(director__contains=term)
    return movie_results


def processQueryJson(query):
    movie_results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        movie_results += Movie.objects.filter(name__contains=term).values()
        movie_results += Movie.objects.filter(director__contains=term).values()
    return movie_results