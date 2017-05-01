from django.shortcuts import render
from django.http import HttpResponse 
from . import models  
# Create your views here.
def index(request):
	article = models.Article.objects.get(pk=1)  
	return render(request,'index.html',{'tip': article})

def message(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	comments = request.POST.get('comments')
	models.Message.objects.create(name=name, email=email, comments=comments)
	return render(request, 'index.html')