# -*- coding: utf-8 -*-
# GNU General Public License v2.0 (see COPYING or https://www.gnu.org/licenses/gpl-2.0.txt)

# pylint: disable=invalid-name,missing-docstring

from __future__ import absolute_import, division, print_function, unicode_literals
import unittest
from resources.lib import utils

xbmc = __import__('xbmc')
xbmcaddon = __import__('xbmcaddon')
xbmcgui = __import__('xbmcgui')
xbmcvfs = __import__('xbmcvfs')


class TestLocalizeDate(unittest.TestCase):

    def test_localize_date_none_returns_empty(self):
        self.assertEqual(utils.localize_date(None), '')

    def test_localize_date_empty_string_returns_empty(self):
        self.assertEqual(utils.localize_date(''), '')

    def test_localize_date_int_year_returns_string_year(self):
        self.assertEqual(utils.localize_date(2006), '2006')

    def test_localize_date_string_year_returns_string_year(self):
        self.assertEqual(utils.localize_date('2006'), '2006')

    def test_localize_date_float_year_returns_string(self):
        self.assertEqual(utils.localize_date(2006.0), '2006.0')
