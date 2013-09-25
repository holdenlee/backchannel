from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    #text of comment
    text = models.TextField()
    #time in seconds
    #eventually change this to comparable?
    video_time = models.IntegerField()
    #time published
    pub_time=models.DateTimeField('time published')
    #user who submitted comment
    #user = models.CharField(max_length=20)
    user = models.ForeignKey(User, blank=True, null=True)
    #votes
    votes=models.IntegerField(default=0)
    #id number.
    #id_num= models.IntegerField(default=0)
    #whether this comment is resolved
    resolved = models.BooleanField()
    tags=TaggableManager()
    #type?

    def __unicode__(self):
        return self.text
    

#almost everything here is the same except video_time, resolved are missing
#and there's a foreign key
#maybe better way of doing this?
class Response(models.Model):
    #each response is associated to only 1 comment
    comment = models.ForeignKey(Comment)
    #text
    text = models.TextField()
    #time published
    pub_time=models.DateTimeField('time published')
    #user who submitted comment
    user = models.CharField(max_length=20)
    #votes
    votes=models.IntegerField(default=0)
    #tags
    tags=TaggableManager()
    #id number. Not necessary because generated automatically
    #id_num= models.IntegerField(default=0)

    def __unicode__(self):
        return self.text

##class Tag(models.Model):
##    text = models.CharacterField(max_length=50)
##    
