#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase



class AdminTest(LiveServerTestCase):

	'''
	Sample functional test for the admin.
	'''
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_admin_site(self):
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django', body.text)

	def tearDown(self):
		self.browser.quit()