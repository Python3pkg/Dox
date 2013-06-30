"""
Command line tool.
"""
import sys
from dox.config import init_environment
from dox.client import ping_library

def init(args):
    """
    Initialize the Dox environment.
    """
    if not (args.library_key and args.project and args.content_type and args.body_field):
        print 'You must specify the library key, project, content type and body field to initialize the environment.'
        sys.exit(1)
    
    print 'Dox -----------------------------------------'
    print 'Initializing environment with:'
    print 'Library Key',args.library_key
    print 'Project',args.project
    print 'Content Type',args.content_type
    print 'Body Field',args.body_field
    print 'Key Field',args.key_field
    print '---------------------------------------------'
    
    init_environment(args)
    
    print 'Environment initialized.'
    
    print 'Testing environment...'
    ping_library()
    print 'Connection settings are good.'

def upload(args):
    """
    Uploads documents.
    """
    print 'Uploading documents...'
