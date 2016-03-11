#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

if [ -f venv/bin/activate ]; then
    source venv/bin/activate
else
   virtualenv venv && \
       source venv/bin/activate && \
       pip install -r requirements.txt
fi

./ics2owncloud.py
