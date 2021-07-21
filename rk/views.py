# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rk . models import Contact_details, Feedback , Book_rooms, Order_food
# Create your views here.
def index(request):
	return render(request,'rk/index.html')
	
def service(request):
	return render(request,'rk/services.html')

def bookroom(request):
	if request.method == "POST":			
		name=request.POST.get('name')
		email=request.POST.get('email')
		accommodation_enquiry=request.POST.get('from1')
		airconditioned_cabin=request.POST.get('to')
		date_of_arrival=request.POST.get('doa')
		number_of_persons=request.POST.get('Number')
		number_of_days=request.POST.get('Number1')
		message=request.POST.get('message1')
		abc32=Book_rooms(name=name,email=email,accommodation_enquiry=accommodation_enquiry,airconditioned_cabin=airconditioned_cabin,date_of_arrival=date_of_arrival,number_of_persons=number_of_persons,number_of_days=number_of_days,message=message)
		abc32.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/bookroom.html')

def feedback(request):
	if request.method == "POST":
		name=request.POST.get('y1')
		email=request.POST.get('y2')
		subject=request.POST.get('subject')
		message=request.POST.get('message')
		abc=Feedback(feedname=name,email=email,subject=subject,message=message)
		abc.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/feedback.html')

def orderfood(request):
	if request.method == "POST":
		name=request.POST.get('Name')			
		email=request.POST.get('email')
		phone_no=request.POST.get('Phoneno')
		address=request.POST.get('address')
		date=request.POST.get('Text')
		time=request.POST.get('t1')
		nofpeople=request.POST.get('t2')
		items1=request.POST.get('t3')
		items2=request.POST.get('t4')
		items3=request.POST.get('t5')
		items4=request.POST.get('t6')
		items=items1 , items2 ,items3, items4
		abc12=Order_food(name=name,email=email,phone_no=phone_no,address=address,date=date,time=time,nofpeople=nofpeople,items=items)
		abc12.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/orderfood.html')
	
def contact(request):
	if request.method == "POST":
		uname=request.POST.get('t1')
		email=request.POST.get('t2')
		message=request.POST.get('t3')
		abc=Contact_details(uname=uname,email=email,msg=message)
		abc.save()
		return render(request,'rk/index.html')
	else:
		return render(request,'rk/contact.html')