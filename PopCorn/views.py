from django.shortcuts import render
from Movie.models import Movie
from User.models import UserProfile
import json
from django.http import HttpResponse
import datetime
from django.core import serializers


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
    results = {}
    # user_results = []
    if query != '':
        temp = processQueryJson(query)
        n = temp.__len__()
        temp2 = processQueryUsersJson(query)
        n2 = temp2.__len__()
        # temp = serializers.serialize("json", temp)
        for i in range(0,n):
            # print(str(i) + temp[i].name)
            results['t' + str(i)] = temp[i]
            # results['t' + str(i)] = serializers.serialize("json", temp[i])
        for i in range(0,n2):
            results['u' + str(i)] = temp2[i]
        # results = serializers.serialize("json", results.get_queryset())
    return HttpResponse(json.dumps(results, default=date_handler), content_type="application/json")
    # return HttpResponse(results, content_type="application/json")


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


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
    results = []
    temp = query.split('+')
    terms = []
    for term in temp:
        terms += term.split(' ')
    for term in terms:
        results += UserProfile.objects.filter(alias__contains=term).values()
    # temp = []
    # for i in range(0,results.__len__()):
    #     flag = True
    #     for j in range(i + 1,results.__len__()):
    #         if results[i] == results[j]:
    #             flag = False
    #             break
    #     if flag:
    #         temp.append(results[i])
    return results


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
    temp = []
    for i in range(0,movie_results.__len__()):
        flag = True
        for j in range(i + 1,movie_results.__len__()):
            if movie_results[i] == movie_results[j]:
                flag = False
                break
        if flag:
            temp.append(movie_results[i])
    return temp