__author__ = "James Alexander Levy (jamesalexanderlevy@gmail.com)"

import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import app_settings, methods


class Index(webapp.RequestHandler):
    """
    Landing Page
    """
    def get(self):
			# set context
			context = {
			  'api_base': 'http://stickybits.com/api/',
			  'apis': methods.API_LIST
			    }
			# calculate the template path
			path = os.path.join(os.path.dirname(__file__), 'templates',
			    'index.html')
			# render the template with the provided context
			self.response.out.write(template.render(path, context))


# wire up the views
application = webapp.WSGIApplication([
    ('/', Index)

], debug=True)

def main():
    "Run the application"
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
