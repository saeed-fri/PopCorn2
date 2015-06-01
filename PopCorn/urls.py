from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'PopCorn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comment/(?P<post_id>\d+)/(?P<user_id>\d+)/', 'Post.views.comment'),
    url(r'^like/(?P<post_id>\d+)/(?P<user_id>\d+)/', 'Post.views.like'),
    url(r'^unlike/(?P<post_id>\d+)/(?P<user_id>\d+)/', 'Post.views.unlike'),
    url(r'^movie/(?P<movie_id>\d+)/', 'Movie.views.movie'),
    url(r'^search/(?P<query>[a-zA-Z0-9+\ ]*)', 'PopCorn.views.search'),
    url(r'^post/(?P<post_id>\d+)/', 'Post.views.post'),
    url(r'^timeline/', 'Post.views.timeline'),
    url(r'^register/', 'User.views.register'),
    url(r'^forgot/', 'User.views.forgot'),
    url(r'^user/', 'User.views.profile'),
    url(r'^related/', 'User.views.related_user'),
    url(r'^login/', 'User.views.sign_in'),
    url(r'^search_ajax/', 'PopCorn.views.search_ajax')
]
