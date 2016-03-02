from django.conf.urls import patterns, url, include
from lpage import views

urlpatterns = patterns('',
	# Main MPG Website URLs
	url(r'^send-lead$', views.send_lead),
	url(r'^send-lead/(?P<client>[\w_-]+)$', views.send_lead),
	url(r'^new/$', views.home),
	url(r'^$', views.index),

	# Landing Pages URLs
	url(r'estadao/$', views.estadao),
	url(r'hinode/$', views.hinode),
	url(r'espm/$', views.espm),
	url(r'^(?P<slug>[\w_-]+)/(?P<template>[\w_-]+)$', views.page),
)