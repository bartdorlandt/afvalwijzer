Afvalwijzer library
===================

|PyPi Status| |Build Status| |Coverage Status| |Wheel Status| |Python versions|

This library is meant to interface with `mijnafvalwijzer <http://www.mijnafvalwijzer.nl/>`__.

It is meant as a *workaround* for the afvalwijzer app (used in the Netherlands) to be notified when to place the bin at the road.
Since this app delivers a poor functionality for notifications, and I needed a small project, I created this.

Installation
------------

.. code:: bash

    pip install afvalwijzer

Uninstallation
--------------

.. code:: bash

    pip uninstall afvalwijzer

Usage
-----

.. code:: python

    >>> from Afvalwijzer import Afvalwijzer
    >>> zipcode = '3564KV'
    >>> number = '13'
    >>> garbage = Afvalwijzer(zipcode, number)

    >>> garbage.pickupdate
    'Vandaag'

    >>> garbage.wastetype
    'Groente-, Fruit- en Tuinafval'

    >>> garbage.garbage
    ('Vandaag', 'Groente-, Fruit- en Tuinafval')

The following function only returns true if the pickup date is the same as today.

.. code:: python

    >>> garbage.notify
    True

Below is shown how I use it to get notified using pushbullet.

.. code:: python

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
    pickupdate, wastetype = garbage.garbage
    notify = garbage.notify
    if notify and pushbulletapi:
        notification(pushbulletdevice)

Cron job
--------
This script can now be set up as a cronjob on your server or alike.

.. code:: bash

    0 6 * * * cd /path/to/script/notify_garbage.py > /dev/null 2>&1

Caveat
------
* Output is provided in Dutch due to the main website. There is a button for English, but I haven't got it working (yet).

Contributors are most welcome
-----------------------------
* I'm still learning how to work with it all. Therefore feedback, advice, pull request etc. are most welcome.

.. |Wheel Status| image:: https://img.shields.io/pypi/wheel/afvalwijzer.svg
   :target: https://pypi.python.org/pypi/afvalwijzer
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/afvalwijzer.svg
   :target: https://pypi.python.org/pypi/afvalwijzer
.. |PyPi Status| image:: https://img.shields.io/pypi/v/afvalwijzer.svg
   :target: https://pypi.python.org/pypi/afvalwijzer
.. |Build Status| image:: https://travis-ci.org/bambam82/afvalwijzer.svg?branch=master
   :target: https://travis-ci.org/bambam82/afvalwijzer
.. |Coverage Status| image:: https://coveralls.io/repos/github/bambam82/afvalwijzer/badge.svg?branch=master
   :target: https://coveralls.io/github/bambam82/afvalwijzer?branch=master

