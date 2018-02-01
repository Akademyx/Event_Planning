# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    street_address = models.CharField(max_length=255)
    city_province = models.CharField(max_length=255)

class Event(models.Model):
    event_type = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    event_date = models.DateField(auto_now_add=False)
    event_time = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Attendee(models.Model):
    attending = models.BooleanField()
    events = models.ForeignKey(Event, related_name="event_attendees")
    participants = models.ForeignKey(Person, related_name="event_attendees")

    