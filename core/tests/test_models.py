#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.test import TestCase
from core.models import Jobs, Items, People



class JobsModelTest(TestCase):

    '''
    Sample functional test for the model jobs.
    '''

    def setUp(self):
        self.job = Jobs.objects.get_or_create(
            name='Python Developer Python', description='programador',
            )

    def test_defaults_jobs(self):
        jobs = Jobs()
        self.assertEqual(jobs.id_jobs, None)
        self.assertEqual(jobs.name, '')
        self.assertEqual(jobs.description, '')

    def test_created_jobs(self):
        self.assertEqual(Jobs.objects.count(), 1)

    def test_list_jobs(self):
        jobs = Jobs()
        self.assertTrue(jobs.jobs(True))
        self.assertFalse(jobs.jobs(False))
    
    def tearDown(self): 
        del self.job



class ItemsModelTest(TestCase):

    '''
    Sample functional test for the model items.
    '''

    def setUp(self):
        self.item = Items.objects.get_or_create(
            html=1, python=1,
            css=1,android=1,
            ios=1,js=1,
            django=1, description='evaluation')

    def test_defaults_items(self):
        item = Items()
        self.assertEqual(item.id_item, None)
        self.assertEqual(item.html, None)
        self.assertEqual(item.python, None)
        self.assertEqual(item.css, None)
        self.assertEqual(item.android, None)
        self.assertEqual(item.ios, None)
        self.assertEqual(item.js, None)
        self.assertEqual(item.django, None)
        self.assertEqual(item.description, '')

    def test_created_items(self):
        self.assertEqual(Items.objects.count(), 1)
    
    def tearDown(self): 
        del self.item



class PeopleModelTest(TestCase):

    '''
    Sample functional test for the model people.
    '''

    def setUp(self):

        self.people = People.objects.get_or_create(
            first_name='Henrique',last_name='Luz Rodrigues',
            email='henrique.lr89@gmail.com',description='programador')
        
    def test_defaults_people(self):
        people = People()
        self.assertEqual(people.id_people, None)
        self.assertEqual(people.first_name, '')
        self.assertEqual(people.last_name, '')
        self.assertEqual(people.email, '')
        self.assertEqual(people.description, '')

    def test_created_People(self):
        self.assertEqual(People.objects.count(), 1)
    
    def tearDown(self): 
        del self.people



class ManyToManyTest(TestCase):

    '''
    This sample test for model ManyToMany.
    '''
    
    def setUp(self):
        self.item = Items(
            html=1, python=1,
            css=1,android=1,
            ios=1,js=1,
            django=1, description='evaluation')
        
        self.job = Jobs(
            name='Python Developer', description='developer')

        self.people = People(
            first_name='Henrique',last_name='Luz Rodrigues',
            email='henrique.lr89@gmail.com',description='developer')

        self.item.save()
        self.job.save()
        self.people.save()
        self.people.evaluation.add(self.item)
        self.people.candidature.add(self.job)

    def test_created_people(self):
        self.assertEqual(People.objects.count(),1)

    def test_created_items(self):
        self.assertEqual(Items.objects.count(),1)

    def test_created_jobs(self):
        self.assertEqual(Jobs.objects.count(),1)

    def test_created_people_items(self):
        self.assertTrue(People.objects.filter(evaluation__id_item=self.item.id_item))

    def test_created_people_jobs(self):
        self.assertTrue(People.objects.filter(candidature__id_jobs=self.job.id_jobs))
    
    def tearDown(self): 
        del self.item
        del self.job
        del self.people