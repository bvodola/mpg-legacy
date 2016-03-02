import requests, json
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
from .models import GlobalData, ESPMCourse

def index(request):
	data = GlobalData.objects.all() # Grab global data of the website
	return render(request,'lpage/index.html', {'data': data})

def home(request):
	data = GlobalData.objects.all() # Grab global data of the website
	return render(request,'creative/index.html', {'data': data})

def page(request,slug,template):

	# Gets the version of the page (for minor changes to the page layout)
	try:
		request.GET.get('version')
	except NameError:
		version = 'a'
	else:
		version = request.GET.get('version')

	return render(request,slug+'/'+template+'.html', {'version': version})

def estadao(request):
	return render(request,'estadao/index.html')

def hinode(request):
	return render(request,'hinode/1.html')

def espm(request):
	courses = ESPMCourse.objects.all()
	return render(request, 'espm/1.html', {'courses': courses})

def send_lead(request, client = ""):

	# Cheks if the request is a POST
	if(request.method == 'POST'):

		# Fetch the attributes from the POST request
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')

		if(client == ""):
			client = request.POST.get('client')

		# Try DDD
		try:
			request.POST.get('ddd')
		except NameError:
			ddd = ''
		else:
			ddd = request.POST.get('ddd')

		# Try Period
		try:
			request.POST.get('period')
		except TypeError:
			period = ''
		else:
			period = request.POST.get('period')

		# Try CPF
		try:
			request.POST.get('cpf')
		except NameError:
			cpf = ''
		else:
			cpf = request.POST.get('cpf')

		# Try Message
		try:
			request.POST.get('message')
		except NameError:
			content = ''
		else:
			content = request.POST.get('message')

		# Try Lead.obs
		try:
			request.POST.get('obs')
		except NameError:
			obs = ''
		else:
			obs = request.POST.get('obs')

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
		elif (client == 'anderson-hinode'):
			subject = '[MPG] Lead Hinode'
			content = 'Nome: '+name+"\n"+'Telefone: '+phone+"\n"+'Email: '+email+"\n"+'Melhor Horário: '+period+"\n"
			sender = 'hinode@mediaplanning.com.br'
			to = ['bvodola@gmail.com']
			headers = {'Reply-To': email}
			template = 'hinode/confirm.html'

			# Saves the Lead on Lead Manager API
			auth_header = {'Authorization': 'Token '+settings.LM_API_TOKEN}
			payload = {'name': name, 'phone1': phone, 'email': email, 'cpf': cpf, 'best_period': period, 'client': settings.LM_API_URL+'users/5/'}
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