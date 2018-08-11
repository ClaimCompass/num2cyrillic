# (C) Copyright 2018 ClaimCompass, Inc.
#
# This file is part of num2cyrillic.
#
# num2cyrillic is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# num2cyrillic is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with num2cyrillic.  If not, see <https://www.gnu.org/licenses/>

# Original author: Kouber Saparev
# Python implementation by: vshulev / ClaimCompass, Inc
# https://github.com/ClaimCompass/num2cyrillic


import unittest
from num2cyrillic import NumberToWords

        
class TestCyrillicMethod(unittest.TestCase):

    def test_single(self):
        num2bg = NumberToWords()
        self.assertEqual(num2bg.cyrillic(3), "три")
        
    def test_zero(self):
        num2bg = NumberToWords()
        self.assertEqual(num2bg.cyrillic(0), "нула")

    def test_nil(self):
        num2bg = NumberToWords()
        self.assertEqual(num2bg.cyrillic(), "")
       
    def test_twodigit(self):
        num2bg = NumberToWords()
        self.assertEqual(num2bg.cyrillic(67), "шестдесет и седем")

        
def test_all():
    unittest.main()
    
if __name__ == '__main__':
    test_all()
