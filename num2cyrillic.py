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



class NumberToWords:
    locale = 'bg'
    lang = 'Bulgarian'
    lang_native = 'Български'
    _misc_strings = {
        'deset': 'десет',
        'edinadeset': 'единадесет',
        'na': 'на',
        'sto': 'сто',
        'sta': 'ста',
        'stotin': 'стотин',
        'hiliadi': 'хиляди',
    }
    _digits = {
        0: [None, 'едно', 'две', 'три', 'четири', 'пет', 'шест', 'седем', 'осем', 'девет'],
        1: [None, 'един', 'два', None, None, None, None, None, None, None],
        -1: [None, 'една', None, None, None, None, None, None, None, None],
    }
    _digits_initialized = False
    _last_and = False
    _zero = 'нула'
    _infinity = 'безкрайност'
    _and = 'и'
    _sep = ' '
    _minus = 'минус'
    _plural = 'а'
    _exponent = {
        0: '',
        3: 'хиляда',
        6: 'милион',
        9: 'милиард',
        12: 'трилион',
        15: 'квадрилион',
        18: 'квинтилион',
        21: 'секстилион',
        24: 'септилион',
        27: 'октилион',
        30: 'ноналион',
        33: 'декалион',
        36: 'ундекалион',
        39: 'дуодекалион',
        42: 'тредекалион',
        45: 'кватордекалион',
        48: 'квинтдекалион',
        51: 'сексдекалион',
        54: 'септдекалион',
        57: 'октодекалион',
        60: 'новемдекалион',
        63: 'вигинтилион',
        66: 'унвигинтилион',
        69: 'дуовигинтилион',
        72: 'тревигинтилион',
        75: 'кваторвигинтилион',
        78: 'квинвигинтилион',
        81: 'сексвигинтилион',
        84: 'септенвигинтилион',
        87: 'октовигинтилион',
        90: 'новемвигинтилион',
        93: 'тригинтилион',
        96: 'унтригинтилион',
        99: 'дуотригинтилион',
        102: 'третригинтилион',
        105: 'кватортригинтилион',
        108: 'квинтригинтилион',
        111: 'секстригинтилион',
        114: 'септентригинтилион',
        117: 'октотригинтилион',
        120: 'новемтригинтилион',
        123: 'квадрагинтилион',
        126: 'унквадрагинтилион',
        129: 'дуоквадрагинтилион',
        132: 'треквадрагинтилион',
        135: 'кваторквадрагинтилион',
        138: 'квинквадрагинтилион',
        141: 'сексквадрагинтилион',
        144: 'септенквадрагинтилион',
        147: 'октоквадрагинтилион',
        150: 'новемквадрагинтилион',
        153: 'квинквагинтилион',
        156: 'унквинкагинтилион',
        159: 'дуоквинкагинтилион',
        162: 'треквинкагинтилион',
        165: 'кваторквинкагинтилион',
        168: 'квинквинкагинтилион',
        171: 'сексквинкагинтилион',
        174: 'септенквинкагинтилион',
        177: 'октоквинкагинтилион',
        180: 'новемквинкагинтилион',
        183: 'сексагинтилион',
        186: 'унсексагинтилион',
        189: 'дуосексагинтилион',
        192: 'тресексагинтилион',
        195: 'кваторсексагинтилион',
        198: 'квинсексагинтилион',
        201: 'секссексагинтилион',
        204: 'септенсексагинтилион',
        207: 'октосексагинтилион',
        210: 'новемсексагинтилион',
        213: 'септагинтилион',
        216: 'унсептагинтилион',
        219: 'дуосептагинтилион',
        222: 'тресептагинтилион',
        225: 'кваторсептагинтилион',
        228: 'квинсептагинтилион',
        231: 'секссептагинтилион',
        234: 'септенсептагинтилион',
        237: 'октосептагинтилион',
        240: 'новемсептагинтилион',
        243: 'октогинтилион',
        246: 'уноктогинтилион',
        249: 'дуооктогинтилион',
        252: 'треоктогинтилион',
        255: 'кватороктогинтилион',
        258: 'квиноктогинтилион',
        261: 'сексоктогинтилион',
        264: 'септоктогинтилион',
        267: 'октооктогинтилион',
        270: 'новемоктогинтилион',
        273: 'нонагинтилион',
        276: 'уннонагинтилион',
        279: 'дуононагинтилион',
        282: 'тренонагинтилион',
        285: 'кваторнонагинтилион',
        288: 'квиннонагинтилион',
        291: 'секснонагинтилион',
        294: 'септеннонагинтилион',
        297: 'октононагинтилион',
        300: 'новемнонагинтилион',
        303: 'центилион',
    }

    def __init__(self):
        self._init_digits()

    def _init_digits(self):
        if not self._digits_initialized:
            for i in range(3, 10):
                self._digits[1][i] = self._digits[0][i]
            for i in range(2, 10):
                self._digits[-1][i] = self._digits[0][i]
            self._digits_initialized = True

    def _split_number(self, num):
        if isinstance(num, int):
            num = str(num)
        first = []
        if len(num) % 3 != 0:
            if len(num[1:]) % 3 == 0:
                first = [num[0:1]]
                num = num[1:]
            elif len(num[2:]) % 3 == 0:
                first = [num[0:2]]
                num = num[2:]
        ret = [num[i:i+3] for i in range(0, len(num), 3)]
        return first + ret

    def _discard_empties(self, ls):
        return list(filter(lambda x: x is not None, ls))

    def _show_digits_group(self, num, gender=0, last=False):
        num = int(num)
        e = int(num%10)                # ones
        d = int((num-e)%100/10)        # tens
        s = int((num-d*10-e)%1000/100) # hundreds
        ret = [None] * 6

        if s:
            if s == 1:
                ret[1] = self._misc_strings['sto']
            elif s == 2 or s == 3:
                ret[1] = self._digits[0][s] + self._misc_strings['sta']
            else:
                ret[1] =  self._digits[0][s] + self._misc_strings['stotin']

        if d:
            if d == 1:
                if not e:
                    ret[3] = self._misc_strings['deset']
                else:
                    if e == 1:
                        ret[3] = self._misc_strings['edinadeset']
                    else:
                        ret[3] = self._digits[1][e] + self._misc_strings['na'] + self._misc_strings['deset']
                    e = 0
            else:
                ret[3] = self._digits[1][d] + self._misc_strings['deset']

        if e:
            ret[5] = self._digits[gender][e]

        if len(self._discard_empties(ret)) > 1:
            if e:
                ret[4] = self._and
            else:
                ret[2] = self._and

        if last:
            if not s or len(self._discard_empties(ret)) == 1:
                ret[0] = self._and
            self._last_and = True

        return self._sep.join(self._discard_empties(ret))

    def _to_words(self, num=0):
        num_groups = self._split_number(num)
        sizeof_num_groups = len(num_groups)

        ret = [None] * (sizeof_num_groups + 1)
        ret_minus = ''

        if num < 0:
            ret_minus = self._minus + self._sep
        elif num == 0:
            return self._zero

        i = sizeof_num_groups - 1
        j = 1
        while i >= 0:
            if ret[j] is None:
                ret[j] = ''

            _pow = sizeof_num_groups - i

            if num_groups[i] != '000':
                if int(num_groups[i]) > 1:
                    if _pow == 1:
                        ret[j] += self._show_digits_group(num_groups[i], 0, not self._last_and and i) + self._sep
                        ret[j] += self._exponent[(_pow-1)*3]
                    elif _pow == 2:
                        ret[j] += self._show_digits_group(num_groups[i], -1, not self._last_and and i) + self._sep
                        ret[j] += self._misc_strings['hiliadi'] + self._sep
                    else:
                        ret[j] += self._show_digits_group(num_groups[i], 1, not self._last_and and i) + self._sep
                        ret[j] += self._exponent[(_pow-1)*3] + self._plural + self._sep
                else:
                    if _pow == 1:
                        ret[j] += self._show_digits_group(num_groups[i], 0, not self._last_and and i) + self._sep
                    elif _pow == 2:
                        ret[j] += self._exponent[(_pow-1)*3] + self._sep
                    else:
                        ret[j] += self._digits[1][1] + self._sep + self._exponent[(_pow-1)*3] + self._sep

            i -= 1
            j += 1

        ret = self._discard_empties(ret)
        ret.reverse()
        return ret_minus + ''.join(ret)
        
    def cyrillic(self, num=None):
        return '' if num is None else self._to_words(num).strip() 
