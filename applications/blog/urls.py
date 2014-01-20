from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangonotes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'applications.blog.views.posts_list'),
)