#!/bin/env python

import os
from getpass import getpass
import urllib2

filename = os.path.expanduser('~/.dockerhub-ansible-build')

def parse_config():
    try:
        url = open(filename).readlines()[0].strip()
    except:
        url = None

    return url

def save_config(data):
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
    cfg_file.write('%s\n' % data)
    cfg_file.close()

if __name__ == '__main__':
    url = parse_config()
    old_url = url
    while True:
        if not url:
            url = getpass('Enter Trigger URL (will not echo to screen):')

        # Request a build
        try:
            # presence of data forces this to POST
            response = urllib2.urlopen(url, data='build=true')
        except urllib2.HTTPError, e:
            print(e)
            url = None
        else:
            break

    if old_url != url:
        # url updated; save it to config file
        save_config(url)
