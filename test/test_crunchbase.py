#-*- coding: utf-8 -*-

"""
    crunchbase.test
    ~~~~~~~~~~~~~~~

    Test cases for the crunchbase api
"""

import unittest
import os
from crunchbase import Crunchbase

TEST_API_KEY = '8fa4acddmg2pd4d7srh843y7'

class TestCrunchbase(unittest.TestCase):
    
    def test_connection(self):
        cb = Crunchbase(TEST_API_KEY)

    def test_get_company(self):
        cb = Crunchbase(TEST_API_KEY)
        x = cb.company('crunchbase')

