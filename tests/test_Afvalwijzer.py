import pytest
from Afvalwijzer import Afvalwijzer


class TestAfvalwijzer(object):
    def test_zipcode(self):
        garbage = Afvalwijzer('3564KV', 13)
        assert garbage.zipcode == '3564KV'

    def test_incorrect_zipcode(self):
        with pytest.raises(ValueError) as e:
            garbage = Afvalwijzer('35641KV', 13)

    def test_housenumber(self):
        garbage = Afvalwijzer('3564KV', 13)
        assert garbage.housenumber == 13

    def test_housenumber_string(self):
        garbage = Afvalwijzer('3564KV', '13')
        assert garbage.housenumber == '13'

    def test_garbage(self):
        garbage = Afvalwijzer('3564KV', 13)
        date, wastetype = garbage.garbage
        assert type(date) is str, "output is not a string: %r" % date
        assert type(wastetype) is str, "output is not a string: %r" % date

    def test_pickupdate(self):
        garbage = Afvalwijzer('3564KV', 13)
        date = garbage.pickupdate
        assert type(date) is str, "output is not a string: %r" % date

    def test_wastetype(self):
        garbage = Afvalwijzer('3564KV', 13)
        wastetype = garbage.wastetype
        assert type(wastetype) is str, "output is not a string: %r" % wastetype

    def test_pickupdates(self):
        garbage = Afvalwijzer('3564KV', 13)
        date = garbage.pickupdates
        assert type(date) is list, "output is not a string: %r" % date

    def test_wastetypes(self):
        garbage = Afvalwijzer('3564KV', 13)
        wastetype = garbage.wastetypes
        assert type(wastetype) is list, "output is not a string: %r" % wastetype

    def test_notify(self):
        garbage = Afvalwijzer('3564KV', 13)
        if garbage.pickupdate == 'Vandaag':
            assert garbage.notify is True
        else:
            assert garbage.notify is None
