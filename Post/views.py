from django.shortcuts import render
from Post.models import Post, Comment
from django.http import Http404


def post(request, post_id):
    p = Post.objects.filter(id=post_id)
    if p.__len__() > 0:
        p = p[0]
    else:
        raise Http404("Post does not exist")
    movie = p.movie
    comments = Comment.objects.filter(post=p)
    return render(request, "post.html", {
        "post": p,
        'image_address': 'img/posters/' + str(movie.id) + '.jpg',
        "comments": comments,
        "commentsCount": comments.__len__(),
        })


def timeline(request):
    # form = Users(request.POST)
    return render(request, "timeline.html", {
        # 'form': form
        })