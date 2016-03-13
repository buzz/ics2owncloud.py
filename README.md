# ics2owncloud.py

Before ownCloud 9 I was using something like
[this](https://www.birchpress.com/forums/topic/import-calendar-to-owncloud)
to automatically import iCal files to ownCloud. But this stopped
working in ownCloud 9. So I had to come up with something else to make
periodical iCal imports work.

This script downloads iCal files and imports them into ownCloud using CalDAV.

## Requirements

* Virtualenv
* [Ics.py](https://github.com/C4ptainCrunch/ics.py)
* [Requests](http://www.python-requests.org/)

Just make sure the `virtualenv` command is in `$PATH` when running
`ics2owncloud.sh`. Ics.py and Requests are installed automatically.

## Installation

    $ git clone https://github.com/buzz/ics2owncloud.py.git

## Configuration

### Configuration file

Create and edit config file:

    cp ics2owncloud.ini.example ~/.ics2owncloud.ini

A config file with two entries looks like this:

    [DEFAULT]
    username: tom
    password: 123456
    server: https://cloud.example.com/

    [import_a]
    calendar: calendar_xy
    ics_url: https://USER1:XXX@cloud.owncloud.org/index.php/apps/calendar/export.php?calid=6

    [import_b]
    calendar: facebook
    ics_url: https://www.facebook.com/ical/u.php?uid=10000123456789&key=ABCDEFGHIJKL

* `username` - ownCloud user
* `password` - ownCloud password
* `server` - ownCloud server URI
* `calender` - ownCloud calendar name
* `ics_url` - URL to the ICS file to download (can have username:password format)

### Cron job

A cron job comes in handy to periodically import calendars:

    $ crontab -e

This runs the script every 30 minutes:

    */30 * * * * /PATH/TO/ics2owncloud.sh >/dev/null
