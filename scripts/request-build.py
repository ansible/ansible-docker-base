#!/bin/env python

import os
import urllib2

from getpass import getpass
from ConfigParser import SafeConfigParser, NoOptionError

filename = os.path.expanduser('~/.dockerhub-ansible-build')

def parse_config():
    cfg = SafeConfigParser()
    cfg.add_section('Docker hub URLs')
    cfg.read(filename)

    return cfg

def save_config(cfg):
    try:
        mode = os.stat(filename).st_mode
    except OSError, e:
        # If it doesn't exist, we'll just create it
        if e.errno == 2:
            open(filename, 'w').close()
            mode = os.stat(filename).st_mode
        else:
            raise
    if mode != (mode & 0o7777700):
        # Make sure only the user has permissions
        os.chmod(filename, 0o600)
    cfg_file = open(filename, 'w')
    cfg.write(cfg_file)
    cfg_file.close()

if __name__ == '__main__':
    cfg = parse_config()

    if cfg.items('Docker hub URLs'):
        print 'Type in one of the configured repositories:'
    for urls in cfg.items('Docker hub URLs'):
        print '  * %s' % (urls[0])
    if cfg.items('Docker hub URLs'):
        print 'or',
    print 'enter a name for a new docker repository to build'

    user_choice = raw_input(':: ')
    user_choice = user_choice.strip()

    try:
        url = cfg.get('Docker hub URLs', user_choice)
        new_url = False
    except NoOptionError:
        new_url = True
        url = getpass('Enter Trigger URL for %s (will not be displayed):' % user_choice)

    # presence of data forces this to POST
    response = urllib2.urlopen(url, data='build=true')

    # Save the new url as long as we POST'd successfully
    if new_url:
        cfg.set('Docker hub URLs', user_choice, url)
        save_config(cfg)
