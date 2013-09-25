from django.contrib import admin
from comments.models import Comment, Response

class ResponsesInline(admin.StackedInline):
    model=Response
    extra=1

class CommentAdmin(admin.ModelAdmin):
    inlines=[ResponsesInline]
    #accept default ordering
    #fieldsets = [...]
    list_display = ('text', 'video_time', 'pub_time','user', 'votes', 'resolved')
    list_filter=['resolved']
    search_fields=['text']
    #date_hierarchy='pub_time'
    #how to sort?

admin.site.register(Comment, CommentAdmin)
