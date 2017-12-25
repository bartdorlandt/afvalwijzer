# Afvalwijzer library
[![Build Status](https://travis-ci.org/bambam82/afvalwijzer.svg?branch=master)](https://travis-ci.org/bambam82/afvalwijzer)[![Coveralls github](https://img.shields.io/coveralls/bambam82/afvalwijzer.svg)](https://coveralls.io/github/bambam82/afvalwijzer)[![PyPI version](https://img.shields.io/pypi/v/afvalwijzer.svg)](https://pypi.python.org/pypi/afvalwijzer)[![Wheel](https://img.shields.io/pypi/wheel/afvalwijzer.svg)](https://pypi.python.org/pypi/afvalwijzer)[![Python versions](https://img.shields.io/pypi/pyversions/afvalwijzer.svg)](https://pypi.python.org/pypi/afvalwijzer)

This library is meant to interface with http://www.mijnafvalwijzer.nl/

It is meant as a *workaround* for the afvalwijzer app (used in the Netherlands) to be notified when to place the bin at the road.
Since this app delivers a poor functionality for notifications, and I needed a small project, I created this.

## Installation
```bash
# using pip or pip3
pip install afvalwijzer
```

## Uninstallation
```bash
# using pip or pip3
pip uninstall afvalwijzer
```

## Usage
```python
>>> from Afvalwijzer import Afvalwijzer
>>> zipcode = '3564KV'
>>> number = '13'
>>> garbage = Afvalwijzer.Afvalwijzer(zipcode, number)

>>> garbage.pickupdate
'2017-12-27'

>>> garbage.wastetype
'Groente-, Fruit- en Tuinafval'

>>> garbage.garbage
('2017-12-27', 'Groente-, Fruit- en Tuinafval')
```

The following function only returns true if the pickup date is the same as today.
```python
>>> garbage.notify
```

Below is shown how I use it to get notified using pushbullet.
```python
#!/usr/bin/env python3

from Afvalwijzer import Afvalwijzer
from pushbullet import Pushbullet


def notification(device=None):
    pb = Pushbullet(pushbulletapi)
    try:
        mydevice = pb.get_device(device)
    except:
        mydevice = None
    push = pb.push_note(
        "Container: {}".format(wastetype),
        "Container: {}\nDate: {}".format(wastetype, pickupdate),
        device=mydevice)


zipcode = '3564KV'
number = 13
pushbulletapi = 'pushbullet_api_key'
pushbulletdevice = 'LGE Nexus 5X'

garbage = Afvalwijzer(zipcode, number)
pickupdate, wastetype = garbage.garbage()
notify = garbage.notify()
if notify and pushbulletapi:
	notification(pushbulletdevice)
```

## Cron job
This script can now be set up as a cronjob on your server or alike.

```cron
0 6 * * * cd /path/to/script/notify_garbage.py > /dev/null 2>&1
```

## Caveat
* Output is provided in Dutch due to the main website. There is a button for English, but I haven't got it working (yet).

## Contributors are most welcome
I'm still learning how to work with it all. Therefore feedback, advice, pull request etc. are most welcome.

