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
    
    with open(cfg_path,'wb') as cfg_file:
        cfg.write(cfg_file)

def get_cfg():
    """
    Gets the config file.
    """
    cfg = SafeConfigParser()
    cfg_path = os.path.join(dox_dir(),'dox.cfg')

    # Sanity check
    if not os.path.exists(cfg_path):
        raise ValueError('No config file found.  Directory has not been initialized for dox.  Use dox init.')

    cfg.read(cfg_path)
    
    return cfg

