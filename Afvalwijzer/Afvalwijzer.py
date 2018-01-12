# -*- coding: utf-8 -*-

"""
This library is meant to interface with http://www.mijnafvalwijzer.nl/

It is meant as a workaround for the afvalwijzer app (used in the Netherlands)
to be notified when to place the bin at the road. Since this app delivers a
poor functionality for notifications, and I needed a small project,
I created this.

Author: Bart Dorlandt (bart@bamweb.nl)

## Usage

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

>>> garbage.pickupdates
['dinsdag 02 januari', 'dinsdag 02 januari']

>>> garbage.wastetypes
['Groente-, Fruit- en Tuinafval', 'Kerstbomen']

The following function only returns true if the pickup date is the same as today.
>>> garbage.notify
True

"""

import re

import requests
from bs4 import BeautifulSoup


class Afvalwijzer(object):

    def __init__(self, zipcode, housenumber):
        self.housenumber = housenumber

        _zipcode = re.match('^\d{4}[a-zA-Z]{2}', zipcode)
        if _zipcode:
            self.zipcode = _zipcode.group()
        else:
            raise ValueError("Zipcode has a incorrect format. Example: 3564KV")

        self._pickupdates, self._wastetypes = self.__get_data()

    def __get_data(self):
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/{}/'.format(
            self.zipcode, str(self.housenumber))
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        pickupdates = [str(x.text) for x in soup.findAll('p', class_="firstDate")]
        wastetypes = [str(x.text) for x in soup.findAll('p', class_="firstWasteType")]
        return pickupdates, wastetypes

    @property
    def pickupdate(self):
        return self._pickupdates[0]

    @property
    def wastetype(self):
        return self._wastetypes[0]

    @property
    def pickupdates(self):
        return self._pickupdates

    @property
    def wastetypes(self):
        return self._wastetypes

    @property
    def notify(self):
        """If the pickup date is today, return True."""
        if self.pickupdate == 'Vandaag':
            return True

    @property
    def garbage(self):
        """Return both the pickup date and the container type."""
        return self.pickupdate, self.wastetype
