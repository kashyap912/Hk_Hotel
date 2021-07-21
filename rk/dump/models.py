from __future__ import unicode_literals

from django.db import models

# Create your models here.
	
class Contact_details(models.Model):
	uname=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	message=models.CharField(max_length=50)
	
	def __str__ (self):
		return self.email

class Newsletter(models.Model):
	email=models.CharField(max_length=50)
	
	def __str__ (self):
		return self.email