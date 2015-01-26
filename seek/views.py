#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from core.models import Jobs
from forms import FormsPeopleEvaluation
from send import PerfilEmail



def list_jobs(request):
	list_jobs = Jobs.jobs(True)
	return render(request, 'home.html', {'list_jobs':list_jobs})

def detail_jobs(request, *args, **kwargs):
	list_jobs = get_object_or_404(Jobs, pk=kwargs.get('pk'))
	if request.method == 'POST':
		form = FormsPeopleEvaluation(request.POST, instance=list_jobs)

		if form.is_valid():
			people = form.save()	
			perfil_email = PerfilEmail(people)
			send = perfil_email.email_template(perfil_email.check_perfil())

			if perfil_email.send(send):
				messages.success(request, 'Obrigado pelo interesse, enviamos um email para você.')
			else:
				messages.error(request, 'Ocorreu um erro, tente denovo.')

			form = FormsPeopleEvaluation()
			return render(request, 'seek/detail_jobs.html', {'form': form,'list_jobs':list_jobs})
			
		return render(request, 'seek/detail_jobs.html', {'form': form,'list_jobs':list_jobs})

	form = FormsPeopleEvaluation()
	return render(request, 'seek/detail_jobs.html', {'form': form,'list_jobs':list_jobs})

