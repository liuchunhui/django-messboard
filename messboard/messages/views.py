from django.http import HttpResponse,HttpResponseRedirect
from messages.models import Message
from django.template import Context, loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.utils import timezone


def index(request):
    # return HttpResponse("Hello,World.You're at the poll index.")
    latest_message_list = Message.objects.order_by('-date')[:5]
   
    template = loader.get_template('messages/index.html')
    
    # output = ', '.join([m.topic for m in latest_message_list])
    # return HttpResponse(output)
    context = Context({
        'latest_message_list': latest_message_list,
    })
    # return HttpResponse(template.render(context))
    return render(request, 'messages/index.html',context)
     
def details(request,message_id):
    # return HttpResponse("You're looking at poll %s." % message_id)
    try:
       message = Message.objects.get(pk = message_id)
    except Message.DoesNotExist:
        raise Http404
    return render(request,'messages/detail.html',{'message':message})        

def results(request,message_id):
    return HttpResponse("You're looking at the results of poll %s." % message_id)

def delete(request):
    # message_id = request.POST.get("message_id")
    id = request.GET['id']
    m = Message.objects.get(id=id)
    # m = get_object(Message, pk = message_id)
    m.delete()
    return HttpResponseRedirect("/messages") 
  
def add(request):
    topic = request.GET.get('topic')
    m = Message(topic = topic,date = timezone.now()) 
    m.save() 
    return HttpResponseRedirect("/messages")

def addcomment(request):
    tucao = request.GET.get('tucao')
    id = request.GET.get('id')
    m = Message.objects.get(pk=id)
    m.comment_set.create(tucao = tucao,date = timezone.now())
    return HttpResponseRedirect("/messages")
