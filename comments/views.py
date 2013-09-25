# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
#login
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from comments.models import Comment, Response

from taggit.utils import parse_tags

#every time you add a method add a corresponding url which executes that method
#at comments/url.py

class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'comments_list'

    def get_queryset(self):
        """
        Return the comments ordered by video time.
        """
        return Comment.objects.order_by('video_time')
    #.filter(
    #        pub_date__lte=timezone.now()
    #    ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Comment
    template_name = 'comments/detail.html'
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Comment.objects

def submit(request):
    #get submitted text
    #now create a new Comment
    tags=request.POST['tags']
    li=parse_tags(tags)
    c=Comment.objects.create(text=request.POST['comment_text'],
                           video_time=request.POST['video_time'],
                           pub_time=timezone.now(),
                           user=request.user,
                           votes=0,
                           resolved=(request.POST['type']!="question"))
    for t in li:
        c.tags.add(t)
    c.save()
    #add tags!
    return HttpResponseRedirect(reverse('comments:index', args=()))

def upvote(request,comment_id):
    c = get_object_or_404(Comment, pk=comment_id)
    try:
        c.votes+=1
    except (KeyError, Comment.DoesNotExist):
        pass
    c.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('comments:index', args=()))

def downvote(request,comment_id):
    c = get_object_or_404(Comment, pk=comment_id)
    try:
        c.votes-=1
    except (KeyError, Comment.DoesNotExist):
        pass
    c.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('comments:index', args=()))

def resolve(request, comment_id):
    c = get_object_or_404(Comment, pk=comment_id)
    try:
        c.resolved=True
    except (KeyError, Comment.DoesNotExist):
        pass
    c.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('comments:index', args=()))

def edit(request, comment_id):
    c = get_object_or_404(Comment, pk=comment_id)
    print "editing"
    try:
        #print request.POST
        tags=request.POST['tags']
        li=parse_tags(tags)
        c.text=request.POST['comment_text']
        res=request.POST['resolved']
        #print "Res?"
        #print res
        if res=='yes':
            c.resolved=True
        else:
            c.resolved=False
        c.tags.clear()
        for t in li:
            c.tags.add(t)
    except (KeyError, Comment.DoesNotExist):
        pass
    c.save()
    #add tags!
    return HttpResponseRedirect(reverse('comments:index', args=()))


def fetch_comments(request):
    start_from=0
    if 'start_from' in request.POST:
        start_from=request.POST['start_from']
    comments_list = Comment.objects.filter(video_time__gte=start_from)
    user_filter={}
    if 'user' in request.POST and request.POST['user']!='':
        comments_list = comments_list.filter(user__username__exact=request.POST['user'])
    if 'tags' in request.POST and request.POST['tags']!='':
        # implement tag filters
        tag_list=parse_tags(request.POST['tags'])
        #for tag in tag_list:
        comments_list = comments_list.filter(tags__name__in=tag_list)
    comments_list=comments_list.order_by('video_time')
    #comments_list = Comment.objects.order_by('video_time')
    return render_to_response('comments_template.html',{'comments_list':comments_list})
    #return HttpResponse(data)

#https://docs.djangoproject.com/en/1.6/topics/auth/default/
def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
    return HttpResponseRedirect(reverse('comments:index', args=()))

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('comments:index', args=()))

