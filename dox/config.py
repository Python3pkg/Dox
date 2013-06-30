"""
Config for Dox.
"""
from ConfigParser import SafeConfigParser
import os.path
from os import getcwd, mkdir, remove

def dox_dir():
    """
    Gets or creates the .dox directory.
    """
    dox_dirpath = os.path.join(getcwd(),'.dox')
    
    if not os.path.exists(dox_dirpath):
        mkdir(dox_dirpath)
    
    return dox_dirpath

def init_environment(args):
    """
    Initializes the environment.
    """
    # TODO - Ping Axilent to test settings
    
    dirpath = dox_dir()
    
    cfg_path = os.path.join(dirpath,'dox.cfg')
    
    # Clean out previous config
    if os.path.exists(cfg_path):
        remove(cfg_path)
    
    # New Config File
    cfg = SafeConfigParser()
    cfg.add_section('Connection')
    cfg.set('Connection','endpoint',args.endpoint)
    cfg.set('Connection','library_key',args.library_key)
    cfg.set('Connection','project',args.project)
    cfg.set('Connection','content_type',args.content_type)
    cfg.set('Connection','body_field',args.body_field)
    if args.key_field:
        cfg.set('Connection','key_field',args.key_field)
    
    cfg_file = open(cfg_path,'w')
    cfg.write(cfg_file)
    cfg_file.close()
    