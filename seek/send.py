#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from core.models import Items
from django.template.loader import get_template
from django.template import Context
from evaluation import settings
from django.core.mail import EmailMultiAlternatives



class PerfilEmail(object):

	'''
	This class creates a profile object, to send email accordance 
	with a certain rating.
	'''
	
	def __init__(self, people):
		self.people = people
		self.list_perfil = []
		self.context = {}

	def check_perfil(self):
		evaluation = Items.objects.get(people__id_people=self.people.id_people)
		
		html,css,js = evaluation.html, evaluation.css, evaluation.js
		django, python = evaluation.django, evaluation.python
		ios, android = evaluation.ios, evaluation.android

		if all(items >= 7 for items in (html, css, js)):
			self.list_perfil.append('front')

		if all(items >= 7 for items in (django, python)):
			self.list_perfil.append('back')

		if all(items >= 7 for items in (ios, android)):
			self.list_perfil.append('mobile')

		return self.list_perfil

	def email_template(self, perfil):
		for person in perfil:
			self.context[str(person)] = True
		return get_template('email.html').render(Context(self.context))

	def send(self, template):
		try:
			subject, from_email, to = 'Avaliação', settings.EMAIL_HOST_USER, str(self.people.email).split(',')
			email=EmailMultiAlternatives(subject, 'meus_pedidos', from_email, to)
			email.attach_alternative(template, "text/html")
			return email.send()
		except:
			return False