from django.http import Http404
from django.shortcuts import render
from User.models import UserProfile
from Post.models import Post, Comment, Like
from django.http import Http404
from django.http import HttpResponse


def like(request, post_id, user_id):
    r_post = Post.objects.filter(id=post_id)
    if r_post.__len__() > 0:
        r_post = r_post[0]
    else:
        raise Http404("no such post!")
    user = UserProfile.objects.filter(id=user_id)
    if user.__len__() > 0:
        user = user[0]
    else:
        raise Http404("no such user!")
    Like(post=r_post, user=user).save()
    return HttpResponse("Success!")


def unlike(request, post_id, user_id):
    r_post = Post.objects.filter(id=post_id)
    if r_post.__len__() > 0:
        r_post = r_post[0]
    else:
        raise Http404("no such post!")
    user = UserProfile.objects.filter(id=user_id)
    if user.__len__() > 0:
        user = user[0]
    else:
        raise Http404("no such user!")
    like = Like.objects.filter(post=r_post, user=user)
    for l in like:
        l.delete()
    return HttpResponse("Success!")


def comment(request, post_id, user_id):
    r_post = Post.objects.filter(id=post_id)
    if r_post.__len__() > 0:
        r_post = r_post[0]
    else:
        raise Http404("no such post!")
    author = UserProfile.objects.filter(id=user_id)
    if author.__len__() > 0:
        author = author[0]
    else:
        raise Http404("no such user!")
    text = request.GET['text']
    if text == '':
        raise Http404("no comment text!")
    new_comment = Comment(author=author, post=r_post, text=text)
    new_comment.save();
    return HttpResponse("Success!")


def post(request, post_id):
    p = Post.objects.filter(id=post_id)
    if p.__len__() > 0:
        p = p[0]
    else:
        raise Http404("Post does not exist")
    movie = p.movie
    comments = Comment.objects.filter(post=p)
    likes = Like.objects.filter(post=p)
    return render(request, "post.html", {
        "post": p,
        'image_address': 'img/posters/' + str(movie.id) + '.jpg',
        "comments": comments,
        "commentsCount": comments.__len__(),
        "likeCount": likes.__len__(),
        })


def timeline(request):
    # form = Users(request.POST)
    return render(request, "timeline.html", {
        # 'form': form
        })