import webapp2

# For using google users service
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write('Welcome to TST<br>')
            self.response.write('My name is %s!<br>' % user.nickname())
            self.response.write('<a href="%s">upload file</a><br>' % self.request.url)
            self.response.write('<a href="%s">Sign Out</a><br>' % users.create_logout_url(self.request.url))
        else:
            self.redirect(users.create_login_url(self.request.url))


class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        blob_info = upload_files[0]

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Upload Done</h1>')
        self.response.write('<a href="%s">Main Page</a>' % ('/'))


class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def post(self):
        resource = self.request.get('resource')
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)


class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        resource = self.request.get('resource')
        blob_info = blobstore.get(resource)
        blob_info.delete()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Delete Done</h1>')
        self.response.write('<a href="%s">Main Page</a>' % ('/'))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/myS3/upload', UploadHandler),
    ('/myS3/download', DownloadHandler),
    ('/myS3/delete', DeleteHandler)
], debug=True)
