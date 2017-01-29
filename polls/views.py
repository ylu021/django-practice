from django.shortcuts import render

from django.http import HttpResponse

#Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	return HttpResponse("You are look at question %s." % question_id)

def results(request, question_id):
	return HttpResponse("You are looking at the results of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." % question_id)

