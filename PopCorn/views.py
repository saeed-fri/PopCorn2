from django.shortcuts import render


def search(request):
    # form = Users(request.POST)
    return render(request, "search_results.html", {
        # 'form': form
        })