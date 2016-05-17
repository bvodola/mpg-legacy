#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .models import GlobalData, ESPMCourse

def index(request):
	data = GlobalData.objects.all() # Grab global data of the website
	return render(request,'mpg/index.html', {'data': data})

def page(request,slug,template):

	# Creates the context that will be passed to the template
	context = {}

	# Gets the version of the page (for minor changes to the page layout)
	if request.GET.get('version') is not None:
		context['version'] = request.GET.get('version')
	else:
		context['version'] = 'a'

	# Gets the utm_source parameter from the URL (Performance Marketing Parameter)
	if request.GET.get('utm_source') is not None:
		context['utm_source'] = request.GET.get('utm_source')
	else:
		context['utm_source'] = ''

	# Gets the click_id parameter from the URL (Performance Marketing Parameter)
	if request.GET.get('click_id') is not None:
		context['click_id'] = request.GET.get('click_id')
	else:
		context['click_id'] = ''

	# Gets the gclid parameter from the URL (Performance Marketing Parameter)
	if request.GET.get('gclid') is not None:
		context['gclid'] = request.GET.get('gclid')
	else:
		context['gclid'] = ''

	# Renders the template
	return render(request,slug+'/'+template+'.html', context)

def estadao(request):
	return render(request,'estadao/index.html')

def espm(request):
	courses = ESPMCourse.objects.all()
	return render(request, 'espm/1.html', {'courses': courses})

def send_lead(request, client = ""):

	# Cheks if the request is a POST
	if(request.method == 'POST'):

		if(client == ""):
			client = request.POST.get('client')

		# ==========================================
		# Fetch the attributes from the POST request
		# ==========================================
		
		# Try name
		if request.POST.get('name') is not None:
			name = request.POST.get('name')
		else:
			name = ''

		# Try email
		if request.POST.get('email') is not None:
			email = request.POST.get('email')
		else:
			email = ''

		# Try phone
		if request.POST.get('phone') is not None:
			phone = request.POST.get('phone')
		else:
			phone = ''

		# Try ddd
		if request.POST.get('ddd') is not None:
			ddd = request.POST.get('ddd')
		else:
			ddd = ''
		
		# Try period
		if request.POST.get('period') is not None:
			period = request.POST.get('period')
		else:
			period = ''

		# Try cpf
		if request.POST.get('cpf') is not None:
			cpf = request.POST.get('cpf')
		else:
			cpf = ''

		# Try message
		if request.POST.get('message') is not None:
			message = request.POST.get('message')
		else:
			message = ''

		# Try obs
		if request.POST.get('obs') is not None:
			obs = request.POST.get('obs')
		else:
			obs = ''

		# =======
		# Estadão
		# =======
		if (client == 'estadao'):
			subject = '[MPG] Lead Estadão'
			content = 'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Melhor Horário: '+period+"\n"
			sender = 'estadao@mediaplanning.com.br'
			to = ['vendas.web.estadao@gmail.com', 'diego.cola@estadao.com', 'juvenil.filho@estadao.com', 'luana.sousa@estadao.com']
			headers = {'Reply-To': email}
			template = 'estadao/confirm.html'

			# Saves the Lead on Lead Manager API
			auth_header = {'Authorization': 'Token '+settings.LM_API_TOKEN}
			payload = {'name': name, 'phone1': phone, 'email': email, 'client': settings.LM_API_URL+'users/2/', 'best_period': period}
			req = requests.post(settings.LM_API_URL+'api/leads/', data=payload, headers=auth_header)

			# Creates the message Object
			message = EmailMessage(subject,content,sender,to,headers)

		# ======
		# Hinode
		# ======
		elif (client == 'hinode'):
			subject = '[MPG] Lead Hinode'
			content = 'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Melhor Horário: '+period+"\n"
			sender = 'hinode@mediaplanning.com.br'
			to = ['bvodola@gmail.com']
			headers = {'Reply-To': email}
			template = 'hinode/confirm.html'

			# Saves the Lead on Lead Manager API
			auth_header = {'Authorization': 'Token '+settings.LM_API_TOKEN}
			payload = {'name': name, 'phone1': phone, 'email': email, 'cpf': cpf, 'best_period': period, 'client': settings.LM_API_URL+'users/20/'}
			req = requests.post(settings.LM_API_URL+'leads/', data=payload, headers=auth_header)

			# Creates the message Object
			message = EmailMessage(subject,content,sender,to,headers)

		# ====
		# ESPM
		# ====
		elif (client == 'espm'):
			template = 'espm/confirm.html'

			# Saves the Lead on Lead Manager API
			auth_header = {'Authorization': 'Token '+settings.LM_API_TOKEN}
			payload = {'name': name, 'phone1': phone, 'email': email, 'best_period': period, 'client': settings.LM_API_URL+'users/17/', 'obs': obs}
			req = requests.post(settings.LM_API_URL+'leads/', data=payload, headers=auth_header)

		# =======
		# Vocação
		# =======
		elif (client == 'vocacao'):
			subject = '[MPG] Lead Vocação'
			content = 'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Melhor Horário: '+period+"\n"
			sender = 'vocacao@mediaplanning.com.br'
			to = ['campanha@vocacao.org.br']
			headers = {'Reply-To': email}

			# Try confirm_template
			try:
				request.POST.get('confirm_template')
			except NameError:
				template = 'vocacao/confirm.html'
			else:
				template = request.POST.get('confirm_template')
			

			# Saves the Lead on Lead Manager API
			auth_header = {'Authorization': 'Token '+settings.LM_API_TOKEN}
			payload = {'name': name, 'phone1': phone, 'email': email, 'cpf': cpf, 'best_period': period, 'client': settings.LM_API_URL+'users/18/'}
			req = requests.post(settings.LM_API_URL+'leads/', data=payload, headers=auth_header)

			# Creates the message Object
			# message = EmailMessage(subject,content,sender,to,headers)

		# ======
		# Padrão
		# ======
		else:
			headers = {'Reply-To': email}
			# Creates the message Object
			message = EmailMessage(
					'[MPG] Formulário de Contato', 
					'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Mensagem: '+content,
					'contato@mediaplanning.com.br',
					['contato@mediaplanning.com.br'],
					headers = headers
				)

			# Define Reply-To headers
			headers = {'Reply-To': email}

		# ======================================
		# Sends the message and saves the result
		# ======================================
		try:
			message
		except NameError:
			pass
		else:
			message.send()

		try:
			res
		except NameError:
			res = {}
		else:
			try:
				res['id']
			except KeyError:
				EmailMessage(
					'Lead Manager Error',
					client+': '+str(res),
					'contato@mediaplanning.com.br',
					['bvodola@gmail.com']
				).send()

		# ========================================
		# Checks the json response from the LM API
		# ========================================

		try:
			req
		except NameError:
			req = False
		else:
			pass

		if(req is not False):
			try:
				json.loads(req.text)
			except ValueError:
				res = {}
			else:
				res = json.loads(req.text)

		# ===================================
		# Checks if the template has been set
		# ===================================
		try:
			template
		except NameError:
			return JsonResponse({"lead": res, "success": 1})
		else:
			return render(request,template, {"lead": res})


	# If the request is not a POST, returns the MPG home
	else:
		return render(request,'creative/index.html')