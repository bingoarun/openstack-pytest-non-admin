from authentication import glanceAuthentication
from filewriter import write2file

glance_results = {'key':'value'}

'''
Properties to check -
    status
    image_count
    image_list
    image_upload
    image_delete
    
    
'''

def chkGlanceAuthentication():
    try:
        glance = glanceAuthentication()
    except:
        status = 'ERROR'
    else:
        status = 'SUCCESS'
    return status
    
def printGlanceAuthentication():
    status = chkGlanceAuthentication()
    if ( status == 'SUCCESS' ):
        write2file('STATUS','Authenticated against glance - SUCCESS')
    else:
        write2file('STATUS','Can\'t authenticate against glance - FAILED')

def printGlanceResults():
    printGlanceAuthentication();   
    
printGlanceResults();     