"""
Axilent Client functionality for Dox.
"""
from sharrock.client import HttpClient, ResourceClient, ServiceException
from dox.config import get_cfg

def _get_resource(app,resource,library=True):
    """
    Gets a resource client.
    """
    cfg = get_cfg()
    apikey_setting = 'library_key' if library else 'apikey'
    return ResourceClient('%s/api/resource' % cfg.get('Connection','endpoint'),app,'beta3',resource,auth_user=cfg.get('Connection',apikey_setting))

def _get_client(app,library=True):
    """
    Gets a regular API client.
    """
    cfg = get_cfg()
    apikey_setting = 'library_key' if library else 'apikey'
    return HttpClient('%s/api' % cfg.get('Connection','endpoint'),app,'beta3',auth_user=cfg.get('Connection',apikey_setting))

def get_content_library_resource():
    """
    Gets a content library resource.
    """
    return _get_resource('axilent.library','content')

def get_library_client():
    """
    Gets the library API client.
    """
    return _get_client('axilent.library')

def ping_library():
    """
    Pings the library.
    """
    cfg = get_cfg()
    lib = get_library_client()
    lib.ping(project=cfg.get('Connection','project'),content_type=cfg.get('Connection','content_type'))
