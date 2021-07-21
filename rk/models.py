# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact_details(models.Model):
	uname=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	msg=models.CharField(max_length=40)
	
	def __str__ (self):
		return self.email
		
class Feedback(models.Model):
	feedname=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	subject=models.CharField(max_length=40)
	message=models.CharField(max_length=40)
	
	def __str__ (self):
		return self.email +' ---- '+ self.subject
			
class Book_rooms(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	accommodation_enquiry=models.CharField(max_length=40)
	airconditioned_cabin=models.CharField(max_length=40)
	date_of_arrival=models.CharField(max_length=40)
	number_of_persons=models.CharField(max_length=40)
	number_of_days=models.CharField(max_length=40)
	message=models.CharField(max_length=40)
	
	def __str__(self):
		return self.email + " ---- " + self.accommodation_enquiry
		
class Order_food(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	phone_no=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	date=models.CharField(max_length=40)
	time=models.CharField(max_length=40)
	nofpeople=models.CharField(max_length=40)
	items=models.CharField(max_length=40)
	
	def __str__(self):
		return self.email + " ---- " + self.items