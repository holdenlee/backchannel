from django.conf.urls import patterns, url

from comments import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       #not sure what the name does.
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^(?P<comment_id>\d+)/upvote/$', views.upvote, name='upvote'),
    url(r'^(?P<comment_id>\d+)/downvote/$', views.downvote, name='downvote'),
    url(r'^(?P<comment_id>\d+)/resolve/$', views.resolve, name='resolve'),
    url(r'^(?P<comment_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^fetch_comments/$', views.fetch_comments, name='fetch_comments'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name='log_out'),
)

#what's the syntax of these?
