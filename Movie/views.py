from django.shortcuts import render


def movie(request):
    # form = Users(request.POST)
    return render(request, "movie_profile.html", {
        })