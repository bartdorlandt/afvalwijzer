# -*- coding: utf-8 -*-

'''
This library is meant to interface with http://www.mijnafvalwijzer.nl/

It is meant as a workaround for the afvalwijzer app (used in the Netherlands)
to be notified when to place the bin at the road. Since this app delivers a
poor functionality for notifications, and I needed a small project,
I created this.
'''

import requests
from bs4 import BeautifulSoup
import datetime


class Afvalwijzer(object):

    def __init__(self, zipcode, housenumber):
        self.zipcode = zipcode
        self.housenumber = housenumber
        self._year = datetime.datetime.now().year
        self._today = datetime.date.today()
        self._wastetype = None
        self._pickupdate = None

    def __get_data(self):
        if self._pickupdate and self._wastetype:
            return
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/{}/'.format(
                self.zipcode, self.housenumber)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        dow, day, month = soup.find('p', class_="firstDate").string.split()
        self._wastetype = str(soup.find('p', class_="firstWasteType").string)
        # self._pickupdate = datetime.date(self._year, int(day), int(month))
        self._pickupdate = datetime.datetime.strptime(
            ' '.join((str(self._year), day, month)), '%Y %d %B').date()

    def get_pickupdate(self):
        self.__get_data()
        return self._pickupdate.strftime('%Y-%m-%d')

    def get_wastetype(self):
        self.__get_data()
        return self._wastetype

    def notify(self):
        '''If the pickup date is today, return True.'''
        self.__get_data()
        if self._pickupdate == self._today:
            return True

    def garbage(self):
        '''Return both the pickup date and the container type.'''
        return self.get_pickupdate(), self.get_wastetype()
