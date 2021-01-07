from django.shortcuts import render
from django.http import request
from .models import question
from django.core.paginator import Paginator


def question_list(request,*args):
	ques_all= question.objects.all().order_by('question_number')
	paginations=Paginator(ques_all,1)
	if '' in args:
		pagination=list(paginations)[0]
	elif int(args[0])>10:
		pagination=list(paginations)[9]
	else:
		pagination=list(paginations)[int(args[0])-1]
		
	
	return render (request,'questions/home.html',{'pagination':pagination})
	


