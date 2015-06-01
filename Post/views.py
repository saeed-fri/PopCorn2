from django.shortcuts import render


def post(request):
    return render(request, "post.html", {
        })


def timeline(request):
    # form = Users(request.POST)
    return render(request, "timeline.html", {
        # 'form': form
        })