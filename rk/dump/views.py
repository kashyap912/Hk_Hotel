from django.shortcuts import render
from django.http import HttpResponse
from rk.models import Contact_details,Newsletter
# Create your views here.
def index(request):
	if request.method=="POST":
		email=request.POST.get('r1')
		abc1=Newsletter(email=email)
		abc1.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/index.html')

def services(request):
	return render(request,'rk/services.html')
	
def bookroom(request):
	return render(request,'rk/bookroom.html')
	
def feedback(request):
	return render(request,'rk/feedback.html')
	
def register(request):
	return render(request,'rk/register.html')
	
def contact(request):
	if request.method=="POST":
		name=request.POST.get('t1')
		email=request.POST.get('t2')
		message=request.POST.get('t3')
		abc=Contact_details(uname=name,email=email,message=message)
		abc.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/contact.html')