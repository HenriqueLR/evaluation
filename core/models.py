#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.db import models
from seek.br.br_states import STATE_CHOICES


number = [(x, y) for x in range(0,11) for y in range(0,11) if x == y]



class Jobs(models.Model):

	'''
	This simple class has feature to store jobs, important *status = True 
	open job or False job closed.

	'''

	id_jobs = models.AutoField(primary_key=True, verbose_name=u'Code Jobs', db_column='id_jobs')
	name = models.CharField(max_length=50,verbose_name=u'Name',blank=False,db_column='name')
	description = models.TextField(max_length=200,verbose_name=u'Description',blank=True,
								   db_column='description', default='')
	status = models.BooleanField(verbose_name=u'Status', db_column='status', default=True,
								 blank=True)
	date_created = models.DateTimeField(auto_now_add=True,verbose_name=u'Date Created',blank=False,
										db_column='date_created')

	def __unicode__(self):
		return u'%s' % self.id_jobs

	@staticmethod
	def jobs(status):
		return Jobs.objects.all().filter(status=status).order_by('date_created')

	class Meta:
		verbose_name=u'Job'
		verbose_name_plural=u'Jobs'
		ordering=['id_jobs']
		db_table='jobs'



class Items(models.Model):

	'''
	This simple class, has specific evaluation values according 
	to the project documentation, important feature choices 'number 0 - 10'.
	'''

	id_item = models.AutoField(primary_key=True, verbose_name=u'Code Item', db_column='id_item')
	html = models.IntegerField(verbose_name=u'html',blank=False,db_column='html',choices=number)
	python = models.IntegerField(verbose_name=u'python',blank=False,db_column='python',choices=number)
	css = models.IntegerField(verbose_name=u'css',blank=False,db_column='css',choices=number)
	android = models.IntegerField(verbose_name=u'android',blank=False,db_column='android',choices=number)
	ios = models.IntegerField(verbose_name=u'ios',blank=False,db_column='ios',choices=number)
	js = models.IntegerField(verbose_name=u'js',blank=False,db_column='js',choices=number)
	django = models.IntegerField(verbose_name=u'django',blank=False,db_column='django',choices=number)
	description = models.TextField(max_length=200,verbose_name=u'Description',blank=True,
								   db_column='description', default='')
	date_created = date_created = models.DateTimeField(auto_now_add=True,verbose_name=u'Date Created',blank=False,db_column='date_created')

	def __unicode__(self):
		return u'%s' % self.id_item

	class Meta:
		verbose_name=u'Item'
		verbose_name_plural=u'Items'
		ordering=['id_item']
		db_table='items'



class People(models.Model):

	'''
	This class connects the jobs, the evaluation and people candidates.
	'''

	id_people = models.AutoField(primary_key=True, verbose_name=u'Code People', db_column='id_people')
	first_name = models.CharField(max_length=50,verbose_name=u'First Name',blank=False,db_column='first_name')
	last_name = models.CharField(max_length=50,verbose_name=u'Last Name',blank=False,db_column='last_name')
	email = models.CharField(max_length=50,verbose_name=u'Email',blank=False,db_column='email')
 	city = models.CharField(max_length=30, verbose_name=u'Cidade', db_column='city', blank=True, default='',null=True)
	state = models.CharField(choices=STATE_CHOICES, max_length=10, verbose_name=u'Estado', 
							  db_column='state', blank=True, default='',null=True)
	phone = models.CharField(max_length=20, verbose_name=u'Telefone', db_column='phone', blank=True, 
								default='',null=True)
	mobile_phone = models.CharField(max_length=20, verbose_name=u'Celular', db_column='mobile_phone', blank=True, default='',null=True)
	birth_date = models.DateField(verbose_name=u'Data Nascimento', 
										db_column='birth_date', blank=True,null=True)
	date_created = models.DateTimeField(auto_now_add=True,verbose_name=u'Date Created',blank=False,db_column='date_created')
	description = models.TextField(max_length=200,verbose_name=u'Description',blank=True,
								   db_column='description', default='')
	candidature = models.ManyToManyField('Jobs')
	evaluation = models.ManyToManyField('Items')

	def __unicode__(self):
		return u'%s' % self.id_people

	def display_candidature(self):
		return ', '.join([ candidature.id_jobs for candidature in self.candidature.all() ])
	display_candidature.short_description = 'candidature'
	display_candidature.allow_tags = True

	def display_evaluation(self):
		return ', '.join([ evaluation.id_item for evaluation in self.evaluation.all() ])
	display_evaluation.short_description = 'evaluation'
	display_evaluation.allow_tags = True

	class Meta:
		verbose_name=u'People'
		verbose_name_plural=u'Peoples'
		ordering=['id_people']
		db_table='people'

