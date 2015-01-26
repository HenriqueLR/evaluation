#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django import forms
from core.models import Items, Jobs, People, number

from br.br_states import STATE_CHOICES
from br import forms as brforms

import re
from validate_email import validate_email

from datetime import datetime
from unicodedata import normalize



class FormsPeopleEvaluation(forms.Form):

  '''
  This form has classified fields of jobs model and items, which validates 
  the fields, and forcing fill.
  '''

  first_name = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                               max_length=50, required = True,label='Nome',
    	                         widget=forms.TextInput(attrs={'placeholder': 'Primeiro Nome', 
    	                    	                           	     'class':'form-control',
    	                    	                                 'id':'first_name',
    	                    	                                 'name':'first_name',
    	                    	                                 'type':'text'}))

  last_name = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                               max_length=50, required = True, label='Sobrenome',
                               widget=forms.TextInput(attrs={'placeholder': 'Sobrenome', 
                                                             'class':'form-control',
                                                             'id':'last_name',
                                                             'name':'last_name',
                                                             'type':'text'}))

  email = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                          max_length=200, required = True, label='Email',
                          widget=forms.TextInput(attrs={'placeholder': 'example@example.com', 
                                                        'class':'form-control',
                                                        'id':'email',
                                                        'name':'email',
                                                        'type':'text'}))

  state = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                           required=True, label='Estado',
                           widget=forms.Select(attrs={'class':'form-control', 
                                                      'name':'state', 'id':'state'}, 
                                                      choices=STATE_CHOICES))

  city = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                            max_length=30, required = True, label='Cidade',
                            widget=forms.TextInput(attrs={'placeholder': 'Cidade', 
                                                          'class':'form-control',
                                                          'id':'city',
                                                          'name':'city',
                                                          'type':'text'}))

  phone = brforms.BRPhoneNumberField(error_messages={'required': 'Campo obrigatório.'},
                                        required=True, label='Telefone',
                                        widget=forms.TextInput(attrs={'placeholder': 'ZZ-XXXX-XXXX', 
                                                                  'class':'form-control',
                                                                  'id':'phone',
                                                                  'name':'phone',
                                                                  'type':'text'}))  

  mobile_phone = forms.CharField(error_messages={'required': 'Campo obrigatório.'},
                            required=True, max_length=20, label='Celular',
                            widget=forms.TextInput(attrs={'placeholder': 'ZZ-9XXXX-XXXX', 
                                                          'class':'form-control',
                                                          'id':'mobile_phone',
                                                          'name':'mobile_phone',
                                                          'type':'text'}))

  birth_date = forms.DateField(label='Nascimento', required=True,
                                    error_messages={'required': 'Campo obrigatório.'},
                                    widget=forms.widgets.DateInput(format="%m/%d/%Y", 
                                    attrs={'placeholder': 'dia/mês/ano', 
                                                          'class':'form-control',
                                                          'id':'birth_date',
                                                          'name':'birth_date',
                                                          'type':'text'}))

  description_person = forms.CharField(label='Descrição',
                                error_messages={'required': 'Campo obrigatório.'}, 
                                max_length=200, required = True, 
                                widget=forms.Textarea(attrs={'placeholder': 'Descrição', 
                                                              'class':'form-control',
                                                              'id':'description_person',
                                                              'name':'description_person',
                                                              'type':'text',
                                                              'rows':'3'}))

  html = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='html',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'html', 'id':'html'}, 
                                                    choices=number))

  python = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='python',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'python', 'id':'python'}, 
                                                    choices=number))

  css = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='css',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'css', 'id':'css'}, 
                                                    choices=number))

  android = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='android',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'android', 'id':'android'}, 
                                                    choices=number))

  ios = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='ios',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'ios', 'id':'ios'}, 
                                                    choices=number))

  js = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                         label='javascript',required=True,
                         widget=forms.Select(attrs={'class':'form-control', 
                                                    'name':'js', 'id':'js'}, 
                                                    choices=number))

  django = forms.CharField(error_messages={'required': 'Campo obrigatório.'}, 
                          label='django',required=True,
                          widget=forms.Select(attrs={'class':'form-control', 
                                                      'name':'django', 'id':'django'}, 
                                                      choices=number))

  description_items = forms.CharField(label='Descrição',
                                error_messages={'required': 'Campo obrigatório.'}, 
                                max_length=200, required = True, 
                                widget=forms.Textarea(attrs={'placeholder': 'Descrição', 
                                                              'class':'form-control',
                                                              'id':'description_items',
                                                              'name':'description_items',
                                                              'type':'text',
                                                              'rows':'2'}))

  send = forms.BooleanField(required=False, 
                                widget=forms.TextInput(attrs={'value': 'Enviar', 
                                                              'class':'btn btn-lg btn-success btn-block',
                                                              'id':'send',
                                                              'name':'send',
                                                              'type':'submit'}))

  reset = forms.BooleanField(required=False,
                              widget=forms.TextInput(attrs={'value': 'Limpar', 
                                                            'class':'btn btn-lg btn-success btn-block',
                                                            'id':'reset',
                                                            'name':'reset',
                                                            'type':'reset'}))

  def __init__(self, *args, **kwargs):
    if kwargs.get('instance'):
      self.instance = kwargs.pop('instance')
    super(FormsPeopleEvaluation, self).__init__(*args, **kwargs)

  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name', None)

    if first_name.isdigit():
      raise forms.ValidationError(u'Digite um nome válido.')
    if len(first_name) > 50:
      raise forms.ValidationError(u'Nome muito grande.')
    if not re.match(r"^([a-zA-Z]+)$", first_name):
      raise forms.ValidationError(u"Não pode conter caracteres especiais.")
    return first_name

  def clean_last_name(self):
    last_name = self.cleaned_data.get('last_name', None)
    if last_name.isdigit():
      raise forms.ValidationError(u'Digite um sobrenome válido.')
    if len(last_name) > 50:
      raise forms.ValidationError(u'Nome muito grande.')
    if not re.match(r"^([a-zA-Z ]+)$", last_name):
      raise forms.ValidationError(u"Não pode conter caracteres especiais.")
    return last_name

  def clean_state(self):
    state = self.cleaned_data.get('state', None)
    if state == 'default':
      raise forms.ValidationError(u'Escolha uma das opções.')
    return state

  def clean_city(self):
    city = self.cleaned_data.get('city', None)
    if len(city) > 30:
      raise forms.ValidationError(u'Nome grande demais.')
    if city.isdigit():
      raise forms.ValidationError(u'Digite uma cidade válida.')
    if not re.match(r"^([a-zA-Z ]+)$", city):
      raise forms.ValidationError(u"Não pode conter caracteres especiais.")
    return city

  def clean_email(self):
    email = self.cleaned_data.get('email', None)
    if validate_email(email) == False:
      raise forms.ValidationError(u'Email Inválido.')
    return email

  def clean_mobile_phone(self):
    mobile_phone = self.cleaned_data.get('mobile_phone', None)
    n9 = re.compile(r'^\d{2}-\d{5}-\d{4}$')
    n8 = re.compile(r'^\d{2}-\d{4}-\d{4}$')
    if not (n9.match(mobile_phone) or n8.match(mobile_phone)):
      raise forms.ValidationError(u'ex: XX-9XXXX-XXXX ou XX-XXXX-XXXX')
    return mobile_phone

  def clean_description_person(self):
    description_person = self.cleaned_data.get('description_person', None)
    if description_person.isdigit():
      raise forms.ValidationError(u'Digite uma descrição válida.')
    if len(description_person) > 200:
      raise forms.ValidationError(u'Descrição muito grande.')
    if not re.match(r"^([a-zA-Z ]+)$", description_person):
      raise forms.ValidationError(u"Não pode conter caracteres especiais.")
    return description_person

  def clean_description_items(self):
    description_items = self.cleaned_data.get('description_items', None)
    if description_items.isdigit():
      raise forms.ValidationError(u'Digite uma descrição válida.')
    if len(description_items) > 200:
      raise forms.ValidationError(u'Descrição muito grande.')
    if not re.match(r"^([a-zA-Z ]+)$", description_items):
      raise forms.ValidationError(u"Não pode conter caracteres especiais.")
    return description_items


  def save(self):
    data = self.data.get('birth_date')
    dt = datetime.strptime(data, "%d/%m/%Y").strftime('%Y-%m-%d')

    items = Items(python=self.data.get('python'),html=self.data.get('html'),
                    css=self.data.get('css'),django=self.data.get('django'),
                    js=self.data.get('js'),ios=self.data.get('ios'),
                    android=self.data.get('android'), description=self.data.get('description_items'))
      
    people = People(first_name=self.data.get('first_name').title(),
                      last_name=self.data.get('last_name').title(),
                      email=self.data.get('email'),city=self.data.get('city'),
                      state=self.data.get('state'),phone=self.data.get('phone'),
                      mobile_phone=self.data.get('mobile_phone'),birth_date=dt,
                      description=self.data.get('description_person'))

    items.save()
    people.save()
    people.candidature.add(self.instance)
    people.evaluation.add(items)

    return people