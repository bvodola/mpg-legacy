#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class GlobalData(models.Model):
	name = models.CharField(max_length=100)
	content = models.CharField(max_length=500)
	def __str__(self):
		return self.name+' = '+self.content

class CustomPage(models.Model):
	title = models.CharField(max_length=500)
	def __str__(self):
		return self.title

class CharField(models.Model):
	name = models.CharField(max_length=100)
	content = models.CharField(max_length=500)
	page = models.ForeignKey(CustomPage)
	def __str__(self):
		return ' ['+self.page.title+'] '+self.name+' = '+self.content

class TextField(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	page = models.ForeignKey(CustomPage)
	def __str__(self):
		return ' ['+self.page.title+'] '+self.name+' = '+self.content

class IntegerField(models.Model):
	name = models.CharField(max_length=100)
	content = models.IntegerField()
	page = models.ForeignKey(CustomPage)
	def __str__(self):
		return ' ['+self.page.title+'] '+self.name+' = '+self.content

class ImageField(models.Model):
	name = models.CharField(max_length=100)
	content = models.ImageField(upload_to='uploads')
	page = models.ForeignKey(CustomPage)
	def __str__(self):
		return ' ['+self.page.title+'] '+self.name+' = '+self.content

# ========================
# Clients' Specific Models
# ========================


"""
ESPMCourse
"""
class ESPMCourse(models.Model):

	CATEGORY_CHOICES = (
		('Gestão', 'Gestão'),
		('Digital', 'Digital'),
		('Marketing', 'Marketing'),
	)

	name = models.CharField(max_length=200, default="N/A")
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='uploads', null=True, blank=True)
	starting_date = models.CharField(max_length=200, null=True, blank=True)
	duration = models.CharField(max_length=200, null=True, blank=True)
	price = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name+' ('+self.location+')'+' - '+self.category