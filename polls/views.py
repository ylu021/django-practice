from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader #load template
from .models import Question #use the model

#Create your views here.

def index(request):
	q_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': q_list,
	}
 
	#return HttpResponse("Hello, world. You're at the polls index.")
	return HttpResponse(template.render(context, request)) #render model on template

def detail(request, question_id):
	return HttpResponse("You are look at question %s." % question_id)

def results(request, question_id):
	return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)

