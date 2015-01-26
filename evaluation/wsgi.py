#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evaluation.settings_productions")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()