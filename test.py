# import cloudstorage
# from google.appengine.api import app_identity
# import webapp2
# import os
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/utkarsh1/Documents/cloud-storage-key.json"
# from google.cloud import storage
#
# storage_client = storage.Client()
# bucket_name = 'test-utkarsh-12'
# # bucket_object = storage_client.create_bucket(bucket_name)
# # print bucket_object
#
# bucket_name = os.environ.get(
#             'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
#
# # bucket = storage_client.get_bucket(bucket_name)
# # blob = bucket.blob(destination_blob_name)
# #
# # blob.upload_from_filename(source_file_name)
# #
# # print('File {} uploaded to {}.'.format(
# #     source_file_name,
# #     destination_blob_name

f = open("video.mp4", "r")
print f.read()