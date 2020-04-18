import webapp2

# For using google users service
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.write('Welcome to TST<br>')
			self.response.write('My name is %s!<br>' % user.nickname())
			self.response.write('<a href="%s">Sign Out</a><br>' % users.create_logout_url(self.request.url))
		else:
			self.redirect(users.create_login_url(self.request.url))


app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
