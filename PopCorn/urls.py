from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'PopCorn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/', 'Movie.views.movie'),
    url(r'^search/', 'PopCorn.views.search'),
    url(r'^post/','Post.views.post'),
    url(r'^timeline/', 'Post.views.timeline'),
    url(r'^register/', 'User.views.register'),
    url(r'^forget/', 'User.views.forget'),
    url(r'^user/', 'User.views.profile'),
    url(r'^related/', 'User.views.related_user'),
    url(r'^login/', 'User.views.sign_in'),
]
