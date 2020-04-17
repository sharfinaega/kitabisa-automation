import unittest

from .feature import *

class makeDonation(unittest.TestCase):
    def test_01_load_url(self):
        load_url()
    def test_02_make_donation(self):
        create_donation()
