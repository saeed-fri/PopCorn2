from django.shortcuts import render


def register(request):
    # form = Users(request.POST)
    return render(request, "sign_up.html", {
        # 'form': form
        })


def forgot(request):
    # form = Users(request.POST)
    return render(request, "forgot_password.html", {
        # 'form': form
        })

def profile(request):
    # form = Users(request.POST)
    return render(request, "profile.html", {
        # 'form': form
        })


def related_user(request):
    # form = Users(request.POST)
    return render(request, "related_users.html", {
        # 'form': form
        })


def search(request):
    # form = Users(request.POST)
    return render(request, "search_results.html", {
        # 'form': form
        })


def sign_in(request):
    # form = Users(request.POST)
    return render(request, "sign_in.html", {
        # 'form': form
        })