# ics2owncloud.py

This script downloads iCal files and imports them to ownCloud using CalDAV.

Before ownCloud 9.0 I was using something like
[this](https://www.birchpress.com/forums/topic/import-calendar-to-owncloud)
to automatically import iCal files. After the rewrite of the calendar app
this stopped working. So I had to come up with something else to make
Webcal/iCal subscriptions work.

Webcal subsciptions are also [being worked on](https://github.com/owncloud/calendar/issues/132) in the official calendar app. Once the functionality is available this script becomes obsolete.

*Pull requests welcome!*

## Requirements

* Virtualenv
* [icalendar](https://icalendar.readthedocs.org/) for Python
* [Requests](http://www.python-requests.org/)

Just make sure the `virtualenv` command is in `$PATH` when running
`ics2owncloud.sh`. icalendar and Requests are installed automatically.

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
* `server` - ownCloud server URL
* `calender` - ownCloud calendar name
* `ics_url` - URL to the ICS file to download (can have username:password format)

Don't forget to protect your config file:

    $ chmod 600 ~/.ics2owncloud.ini

### Cron job

A cron job comes in handy to periodically import calendars:

    $ crontab -e

This runs the script every 30 minutes:

    */30 * * * * /PATH/TO/ics2owncloud.sh >/dev/null

