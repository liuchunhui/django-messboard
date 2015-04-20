from django.conf.urls import patterns,url

from messages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<message_id>\d+)/$', views.details, name='details'),
    url(r'^(?P<message_id>\d+)/results/$', views.results, name='results'),
    url(r'delete$', views.delete, name='delete'),
    url(r'add$', views.add, name='add'), 
    url(r'addcomment$', views.addcomment, name='addcomment'),
)

#{% url messages:delete message.id %}
