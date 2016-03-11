#!/usr/bin/env python

from __future__ import print_function
import string
import random
import ConfigParser
from os.path import expanduser, join
import sys

import requests
from ics import Calendar


CALDAVURL = '%sremote.php/dav/calendars/%s/%s/%s.ics'

def do_import(username, password, calendar, server, ics_url):
  c = Calendar(requests.get(ics_url).text)
  for e in c.events:
    caldata = str(Calendar(events=[e]))
    url = CALDAVURL % (server, username, calendar, e.uid)
    r = requests.put(url,
                     data=caldata,
                     auth=(username, password),
                     headers={'content-type':'text/calendar; charset=UTF-8'}
                     )
    r.raise_for_status()
    print('Imported: %s (%d)' % (e.uid, r.status_code), file=sys.stdout)

if __name__ == '__main__':
  Config = ConfigParser.ConfigParser()
  Config.read(join(expanduser('~'), '.ics2owncloud.ini'))
  for key in Config.sections():
    try:
      do_import(Config.get(key, 'username'),
                Config.get(key, 'password'),
                Config.get(key, 'calendar'),
                Config.get(key, 'server'),
                Config.get(key, 'ics_url'),
                )
    except Exception as e:
      print(e, file=sys.stderr)
      print('Error: Could not import: %s' % Config.get(key, 'ics_url'),
            file=sys.stderr)
