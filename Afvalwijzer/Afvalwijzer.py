import requests
from bs4 import BeautifulSoup
import datetime


class Afvalwijzer(object):

    def __init__(self, zipcode, housenumber):
        self.zipcode = zipcode
        self.housenumber = housenumber
        self.year = str(datetime.datetime.now().year)
        self.today = datetime.date.today()
        self.wastetype = None
        self.pickupdate = None

    def __get_data(self):
        if self.pickupdate and self.wastetype:
            return
        url = 'http://www.mijnafvalwijzer.nl/nl/{}/{}/'.format(
                self.zipcode, self.housenumber)
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        dow, day, month = soup.find('p', class_="firstDate").string.split()
        self.wastetype = soup.find('p', class_="firstWasteType").string
        self.pickupdate = datetime.datetime.strptime(
                ' '.join((self.year, day, month)), '%Y %d %B')

    def get_pickupdate(self):
        self.__get_data()
        return self.pickupdate.strftime('%Y-%m-%d')

    def get_wastetype(self):
        self.__get_data()
        return self.wastetype

    def notify(self):
        '''If the pickup date is today, return True.'''
        self.__get_data()
        if self.pickupdate.date() == datetime.datetime.today().date():
            return True

    def garbage(self):
        '''Return both the pickup date and the container type.'''
        return self.get_pickupdate(), self.get_wastetype()
