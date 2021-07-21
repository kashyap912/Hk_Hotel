from django.conf.urls import  url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/', views.index, name="index"),
    url(r'^service/', views.service, name="service"),
    url(r'^bookroom/', views.bookroom, name="bookroom"),
    url(r'^feedback/', views.feedback, name="feedback"),
    url(r'^contact/', views.contact, name="contact"),
	url(r'^orderfood/', views.orderfood, name="orderfood"),
]
