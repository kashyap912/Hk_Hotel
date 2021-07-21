# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Contact_details, Feedback,Book_rooms, Order_food
# Register your models here.

admin.site.register(Contact_details)
admin.site.register(Feedback)
admin.site.register(Book_rooms)
admin.site.register(Order_food)