from django.db import models

class Message(models.Model):
    topic = models.CharField(max_length=500)
    date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.topic

class Comment(models.Model):
    message = models.ForeignKey(Message)
    tucao = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.tucao
