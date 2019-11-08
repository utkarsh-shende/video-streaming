import webapp2
from google.appengine.api import app_identity
# import pdb
# pdb.set_trace()
import os
import cloudstorage
from handler_template import BaseHandler

class MainPage(BaseHandler):
    """Main page for GCS demo application."""


    def get(self):
        self.render_response("index.html")

# [START get_default_bucket]
    def post(self):
        bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
        write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
        filename = "/" + bucket_name + '/' + 'test'
        cloudstorage_file = cloudstorage.open(filename, 'w', content_type="video/mp4", retry_params=write_retry_params)
        upload = self.request.POST['fileToUpload']
        cloudstorage_file.write(upload.file.read())
        cloudstorage_file.close()
        self.redirect("/view-video")