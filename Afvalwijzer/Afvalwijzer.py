# -*- coding: utf-8 -*-

'''
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
>>> garbage = Afvalwijzer.Afvalwijzer(zipcode, number)

>>> garbage.pickupdate
'2017-12-27'

>>> garbage.wastetype
'Groente-, Fruit- en Tuinafval'

>>> garbage.garbage
('2017-12-27', 'Groente-, Fruit- en Tuinafval')

The following function only returns true if the pickup date is the same as today.
>>> garbage.notify

'''

import requests
from bs4 import BeautifulSoup
import datetime

__version__ = '0.2'


class Afvalwijzer(object):

    def __init__(self, zipcode, housenumber):
        self.zipcode = zipcode
        self.housenumber = housenumber
        self._year = datetime.datetime.now().year
        self._today = datetime.date.today()
        self._pickupdate, self._wastetype = self.__get_data()

    def __get_data(self):
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/{}/'.format(
                self.zipcode, self.housenumber)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        dow, day, month = soup.find('p', class_="firstDate").string.split()
        wastetype = str(soup.find('p', class_="firstWasteType").string)
        pickupdate = datetime.datetime.strptime(
            ' '.join((str(self._year), day, month)), '%Y %d %B').date()
        return pickupdate, wastetype

    @property
    def pickupdate(self):
        return self._pickupdate.strftime('%Y-%m-%d')

    @property
    def wastetype(self):
        return self._wastetype

    @property
    def notify(self):
        '''If the pickup date is today, return True.'''
        if self.pickupdate == self._today:
            return True

    @property
    def garbage(self):
        '''Return both the pickup date and the container type.'''
        return self.pickupdate, self.wastetype
