# num2cyrillic

With num2cyrillic.NumberToWords() Python3 class you can convert an integer number
to simple Bulgarian cyrillic words. This can be useful when you need to spell a currency
value e.g. on an invoice.

This is a Python3 porting of the excellent PEAR::Numbers_Words class by [Kouber Saparev](https://github.com/pear/Numbers_Words/blob/master/Numbers/Words/Locale/bg.php) for PHP.

All credit goes to him, this is simply an implementation of the same logic in Python.

## Installation

```
pip install num2cyrillic
```

## Usage

```python
from num2cyrillic import NumberToWords

num2bg = NumberToWords()
num2bg.cyrillic(3)
num2bg.cyrillic(67)

# три
# шестдесет и седем
```

(C) Copyright 2018 ClaimCompass, Inc.