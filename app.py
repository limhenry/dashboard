import os
import jinja2
import webapp2
import json
from google.appengine.api import urlfetch
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

def checkAdmin(self):
    user = users.get_current_user()
    if user:
        if users.is_current_user_admin():
            return True
        else:
			template = JINJA_ENVIRONMENT.get_template('403.html')
			self.response.write(template.render(logout_url = users.create_logout_url('/')))            
    else:
    	self.redirect(users.create_login_url(self.request.uri))

def fetchFirebase(url):

	url = 'https://limhenryxyz.firebaseio.com/' + url + '.json'

	try:
		result = urlfetch.fetch(url)
		if result.status_code == 200:
			if result.content == "null":
				return []
			else:
				return json.loads(result.content)
	except urlfetch.Error:
		logging.exception('Caught exception fetching url')		

class GeneralPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):

			template_values = {
				"active_page": "general",
				'title' : "General"
			}

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class HonorsandawardsPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):
			data = fetchFirebase('honorsandawards')

			template_values = {
				"active_page": "honorsandawards",
				'title' : "Honors and Awards",
				'data': data
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class PresentationsandtalksPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):
			data = fetchFirebase('presentationsandtalks')

			template_values = {
				"active_page": "presentationsandtalks",
				'title' : "Presentations and Talks",
				'data': data
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class ExperiencesPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):
			data = fetchFirebase('experiences')

			template_values = {
				"active_page": "experiences",
				'title' : "Experiences",
				'data': data
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class ProjectsPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):
			data = fetchFirebase('projects')

			template_values = {
				"active_page": "projects",
				'title' : "Projects",
				'data': data
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class SkillsPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):

			template_values = {
				"active_page": "skills",
				'title' : "Skills"
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))

class BlogPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):

			template_values = {
				"active_page": "blog",
				'title' : "Blog"
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))							

class ContactPage(webapp2.RequestHandler):
	def get(self):

		if checkAdmin(self):
			data = fetchFirebase('contact')

			template_values = {
				"active_page": "contact",
				'title' : "Contact",
				'data': data
			}		

			template = JINJA_ENVIRONMENT.get_template('index.html')
			self.response.write(template.render(template_values))


class LogoutPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(users.create_logout_url(self.request.uri))		

app = webapp2.WSGIApplication([
	('/honorsandawards', HonorsandawardsPage), 
	('/presentationsandtalks', PresentationsandtalksPage), 
	('/experiences', ExperiencesPage), 
	('/projects', ProjectsPage), 
	('/skills', SkillsPage), 
	('/blog', BlogPage), 
	('/contact', ContactPage), 
	('/logout', LogoutPage), 
	('/', GeneralPage),
], debug=True)