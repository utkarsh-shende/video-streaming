import webapp2
from google.appengine.api import app_identity
import os


app = webapp2.WSGIApplication(routes=[
    (r'/', 'modules.MainPage.MainPage'),
    (r'/view-video', 'modules.view_video.ViewVideo')
])
