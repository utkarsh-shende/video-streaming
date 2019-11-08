from handler_template import BaseHandler
import cloudstorage
import os
from google.appengine.api import app_identity

class ViewVideo(BaseHandler):
    def get(self):
        # self.response.write()
        page_size=2
        bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
        filename = "/" + bucket_name + '/' + 'test'
        page_size = 5
        stats = cloudstorage.listbucket("/" + bucket_name + '/', max_keys=page_size)
        while True:
            count = 0
            for stat in stats:
                count += 1
                self.response.write(repr(stat))
                self.response.write('\n')

            if count != page_size or count == 0:
                break
        # with cloudstorage.open(filename) as cloudstorage_file:
        #     self.response.write(cloudstorage_file.readline())
        #     cloudstorage_file.seek(-1024, os.SEEK_END)
        #     self.response.write(cloudstorage_file.read())