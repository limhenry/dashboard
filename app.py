import os
import jinja2
import webapp2
import json
from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

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

		template_values = {
			"active_page": "general",
			'title' : "General"
		}

		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

class HonorsandawardsPage(webapp2.RequestHandler):
	def get(self):

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

		template_values = {
			"active_page": "skills",
			'title' : "Skills"
		}		

		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

class BlogPage(webapp2.RequestHandler):
	def get(self):

		template_values = {
			"active_page": "blog",
			'title' : "Blog"
		}		

		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))							

class ContactPage(webapp2.RequestHandler):
	def get(self):

		data = fetchFirebase('contact')

		template_values = {
			"active_page": "contact",
			'title' : "Contact",
			'data': data
		}		

		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/honorsandawards', HonorsandawardsPage), 
	('/presentationsandtalks', PresentationsandtalksPage), 
	('/experiences', ExperiencesPage), 
	('/projects', ProjectsPage), 
	('/skills', SkillsPage), 
	('/blog', BlogPage), 
	('/contact', ContactPage), 
	('/', GeneralPage),
], debug=True)