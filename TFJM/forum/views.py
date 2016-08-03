from django.shortcuts import render, get_object_or_404
from models import Message, Sujet

def message (request, id_message):
	msg = get_object_or_404 (Message, id_message=id_message)
	print (msg)
	return render(request, 'forum/message.html', locals())

def topic (request, id_topic):
	sujet = get_object_or_404 (Sujet, id_topic=id_topic)
	messages = Message.objects.filter (sujet=sujet).order_by ('date_creation')
	return render (request, 'forum/topic.html', locals ())

