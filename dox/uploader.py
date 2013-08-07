"""
Uploads documents to Axilent.
"""
import markdown
from dox.config import get_cfg, get_keymap, get_keyfields
from dox.client import get_content_library_resource, get_library_client

def _tagging(md,content_key,content_type):
    """
    Apply tagging
    """
    tagger = get_library_client()
    
    # tagging
    tags = md.Meta['tags']
    for tag in tags:
        if tag:
            tagger.tagcontent(project='Axilent Docs',
                              content_type=content_type,
                              content_key=content_key,
                              tag=tag)

def upload_document(path,key=None):
    """
    Uploads the specified document, returns the key of the uploaded document.
    """
    # 1. Prepare data for upload
    cfg = get_cfg()
    body_field_name = cfg.get('Connection','body_field')
    data = {}
    md = markdown.Markdown(extensions=['meta','tables'])
    with open(path) as docfile:
        body = md.convert(docfile.read())
        
        for field_name, field_value in md.Meta.items():
            data[field_name] = field_value[0]
        
        data[body_field_name] = body
    
    
    # Upload Content
    return_key = None
    resource = get_content_library_resource()
    if key:
        resource.put(data={'content':data,
                           'content_type':cfg.get('Connection','content_type'),
                           'project':cfg.get('Connection','project'),
                           'key':key})
        
        _tagging(md,key,cfg.get('Connection','content_type'))
        
        return (key,False) # no new document created
    else:
        response = resource.post(data={'content':data,
                                       'project':cfg.get('Connection','project'),
                                       'content_type':cfg.get('Connection','content_type')})
        created_content_type, created_key = response['created_content'].split(':')
        
        _tagging(md,created_key,cfg.get('Connection','content_type'))
        
        return (created_key,True) # new document created
    
def find_key(path,keymap,keyfields):
    """
    Finds a key for the specified document if it exists.
    """
    # First try to pull key from the keymap
    try:
        return keymap[path]
    except KeyError:
        pass
    
    # Try to find it from a keyfield
    try:
        cfg = get_cfg()
        keyfield_name = cfg.get('Connection','key_field')
        md = markdown.Markdown(extensions=['meta','tables'])
        with open(path) as docfile:
            md.convert(docfile.read())
            keyfield = md.Meta[keyfield_name][0]
            return keyfields[keyfield]
    except KeyError:
        pass
    
    # Give up
    return None

def extract_keyfield(path):
    """
    Extracts the keyfield value from the document.
    """
    cfg = get_cfg()
    keyfield_name = cfg.get('Connection','key_field')
    md = markdown.Markdown(extensions=['meta','tables'])
    with open(path) as docfile:
        md.convert(docfile.read())
        try:
            keyfield = md.Meta[keyfield_name][0]
            return keyfield
        except KeyError:
            return None
