from django.shortcuts import render


def post(request):
    # form = Users(request.POST)
    return render(request, "post.html", {
        # 'form': form
        })


def timeline(request):
    # form = Users(request.POST)
    return render(request, "timeline.html", {
        # 'form': form
        })