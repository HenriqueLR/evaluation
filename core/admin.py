#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.contrib import admin
from models import Jobs, Items, People



class JobsAdmin(admin.ModelAdmin):

    '''
    listing the fields of model jobs, in admin application.
    '''

    list_display = ['id_jobs','name','description','date_created','status']
    search_fields = ['name', 'date_created','status']
    list_filter = ['date_created','status']
    admin_order_field = ['id_jobs']



class ItemsAdmin(admin.ModelAdmin):
    
    '''
    listing the fields of model items, in admin application.
    '''

    list_display = ['id_item','html','python','css','android','ios','js','django','date_created']
    search_fields = ['date_created']
    list_filter = ['html','python','css','android','ios','js','django','date_created']
    admin_order_field = ['id_item']



class PeopleAdmin(admin.ModelAdmin):
    
    '''
    listing the fields of model people, in admin application.
    '''
    
    list_display = ['id_people','first_name','last_name','email','date_created','get_candidature']
    search_fields = ['first_name','last_name','email','date_created']
    list_filter = ['date_created']
    admin_order_field = ['id_people']


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(People, PeopleAdmin)