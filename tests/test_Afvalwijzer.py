# import pytest
from Afvalwijzer import Afvalwijzer
import datetime


class TestAfvalwijzer(object):
    def test_zipcode(self):
        garbage = Afvalwijzer('3564KV', 13)
        assert garbage.zipcode == '3564KV'

    def test_housenumber(self):
        garbage = Afvalwijzer('3564KV', 13)
        assert garbage.housenumber == 13

    def test_today(self):
        garbage = Afvalwijzer('3564KV', 13)
        assert type(garbage._today) is datetime.date

    def test_garbage(self):
        garbage = Afvalwijzer('3564KV', 13)
        date, wastetype = garbage.garbage()
        assert type(date) is str, "output is not a string: %r" % date
        assert type(wastetype) is str, "output is not a string: %r" % date

    def test_get_pickupdate(self):
        garbage = Afvalwijzer('3564KV', 13)
        date = garbage.get_pickupdate()
        assert type(date) is str, "output is not a string: %r" % date

    def test_get_wastetype(self):
        garbage = Afvalwijzer('3564KV', 13)
        wastetype = garbage.get_wastetype()
        assert type(wastetype) is str, "output is not a string: %r" % wastetype

    def test_notify(self):
        garbage = Afvalwijzer('3564KV', 13)
        date = garbage._pickupdate
        today = garbage._today
        if date == today:
            assert garbage.notify() is True
