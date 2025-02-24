# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Topic(models.Model):
	top_name = models.CharField(max_length = 256,unique = True)

	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	name = models.CharField(max_length= 256,unique = True)
	url  = models.URLField(unique = True)

	def __str__(self):
		return name

class Access(models.Model):
	name = models.ForeignKey(Webpage,on_delete = models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return str(self.date)


# Create your models here.
