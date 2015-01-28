#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.test import TestCase
from django.core.urlresolvers import reverse
from core.models import Jobs, Items, People
from django.core import mail
from seek.send import ProfileEmail



class ViewJobsTest(TestCase):
    '''
    Testing listing jobs.
    '''
    def setUp(self):
        self.job = Jobs(name='Programador Python', description='programador')
        self.job.save()

        self.url_list_jobs = reverse('list_jobs')

    def test_view_url(self):
        response = self.client.get(self.url_list_jobs)

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, self.url_list_jobs)

    def tearDown(self): 
        del self.job



class ViewJobsDetailTest(TestCase):
    '''
    Testing details jobs and post form validations.
    '''
    def setUp(self):
        self.job = Jobs(name='Programador Python', description='programador')
        self.job.save()

        self.url = reverse('detail_jobs',kwargs={"pk": self.job.id_jobs})

    def test_view_url(self):
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)

    def test_view_form(self):
        response = self.client.post(
            self.url,
                {u'enviar': u'Enviar', u'first_name': u'Henrique', 
                 u'last_name': u'Luz Rodrigues', u'description_person': u'Developer', 
                 u'description_items': u'Developer', u'python': [u'9'], 
                 u'city': u'Castelo', u'ios': u'1', u'birth_date': u'12/12/2014', 
                 u'django': [u'9'], u'html': [u'9'], u'mobile_phone': u'28-99951-2341', 
                 u'phone': u'28-3542-1212', u'js': [u'7'], u'state': [u'AL'], 
                 u'email': u'asdsa@asdas.com', u'css': [u'7'], u'android': [u'7']
            },
            follow=True
        )

        self.assertEquals(People.objects.count(),1)

        self.assertContains(
            response,
            u'Obrigado pelo interesse, enviamos um email para você.'
        )
    
    def test_form_empty(self):
        response = self.client.post(self.url)

        self.assertFormError(
            response,
            'form',
            'last_name',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'first_name',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'description_person',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'description_items',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'python',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'html',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'css',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'js',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'django',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'ios',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'android',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'mobile_phone',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'phone',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'email',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'state',
            u'Campo obrigatório.'
        )

        self.assertFormError(
            response,
            'form',
            'city',
            u'Campo obrigatório.'
        )

    def tearDown(self): 
        del self.job



class TestSend(TestCase):
    '''
    Testing class send.
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

        self.profile_email = ProfileEmail(self.people)

        self.subject = 'Teste'
        self.from_mail = 'henrique.lr89@gmail.com'
        self.to_mail = 'henrique.lr89@gmail.com'
        self.msg = 'Teste'

    def test_list_profile_none(self):
        '''
        Case profile email none alternatives.
        '''
        self.assertFalse(self.profile_email.check_profile())

    def test_list_profile_front(self):
        '''
        Case profile email front-end developer.
        '''
        self.people.evaluation.update(
                    html=7, python=1,
                    css=7,android=7,
                    ios=1,js=7,
                    django=1, description='evaluation')

        self.assertEquals(self.profile_email.check_profile(), ['front'])

    def test_list_profile_back(self):
        '''
        Case profile email back-end developer.
        '''
        self.people.evaluation.update(
                    html=1, python=7,
                    css=1,android=1,
                    ios=1,js=1,
                    django=7, description='evaluation')

        self.assertEquals(self.profile_email.check_profile(), ['back'])

    def test_list_profile_mobile(self):
        '''
        Case profile email mobile developer.
        '''
        self.people.evaluation.update(
                    html=1, python=1,
                    css=1,android=7,
                    ios=7,js=1,
                    django=1, description='evaluation')

        self.assertEquals(self.profile_email.check_profile(), ['mobile'])

    def test_list_profile_all(self):
        '''
        Case profile email all options developer.
        '''
        self.people.evaluation.update(
                    html=7, python=7,
                    css=7,android=7,
                    ios=7,js=7,
                    django=7, description='evaluation')

        self.assertEquals(self.profile_email.check_profile(), ['front','back','mobile'])

    def test_template_mail_none(self):
        '''
        Case email template none profile developer.
        '''
        self.assertTrue(self.profile_email.email_template(self.profile_email.check_profile()))

    def test_template_mail_front(self):
        '''
        Case email template profile front-end developer.
        '''
        self.people.evaluation.update(
                    html=7, python=1,
                    css=7,android=1,
                    ios=1,js=7,
                    django=1, description='evaluation')

        self.assertTrue(self.profile_email.email_template(self.profile_email.check_profile()))

    def test_template_mail_back(self):
        '''
        Case email template profile back-end developer.
        '''
        self.people.evaluation.update(
                    html=1, python=7,
                    css=1,android=1,
                    ios=1,js=1,
                    django=7, description='evaluation')
        
        self.assertTrue(self.profile_email.email_template(self.profile_email.check_profile()))

    def test_template_mail_mobile(self):
        '''
        Case email template profile mobile-end developer.
        '''
        self.people.evaluation.update(
                    html=1, python=1,
                    css=1,android=7,
                    ios=7,js=1,
                    django=1, description='evaluation')
        
        self.assertTrue(self.profile_email.email_template(self.profile_email.check_profile()))

    def test_template_mail_all(self):
        '''
        Case email template all profile developer.
        '''
        self.people.evaluation.update(
                    html=1, python=1,
                    css=1,android=7,
                    ios=7,js=1,
                    django=1, description='evaluation')
        
        self.assertTrue(self.profile_email.email_template(self.profile_email.check_profile()))


    def test_send(self):
        '''
        Testing function to send email
        '''
        self.assertTrue(self.profile_email.send(self.profile_email\
                        .email_template(self.profile_email.check_profile())))

    def tearDown(self): 
        del self.item
        del self.job
        del self.people
