from credentials import *
from pprint import pprint
import glanceclient.v2.client as glclient
glance_endpoint = keystone.service_catalog.url_for(service_type='image')
glance = glclient.Client(glance_endpoint, token=keystone.auth_token)
images = glance.images.list()
#print list(images)
#print "Just a test \n\n\n"
print len(list(images))
#for i in list(images):
#    print i
