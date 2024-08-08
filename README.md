# QLev

<p>

  <a href="https://pypi.org/project/QLev/">
    <img src="https://img.shields.io/pypi/v/QLev"
         alt="PyPI package version">
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/pypi/pyversions/QLev"
         alt="Python versions">
  </a>
  <a href="https://pypi.org/project/QLev/">
    <img src="https://img.shields.io/pypi/dm/QLev.svg?label=PyPI%20downloads"
         alt="PyPI Downloads">
  </a>
</p>

## Introduction
The QLev package is mainly used for:

* Levenshtein distance
* levenshtein distance normalized
* levenshtein distance considering the keyboard keys range 

## Requirements
* Python 3 or later

## Installation
```bash
pip install QLev
```

## Guide

To use simple the levenshtein distance you can:

```python
from QLev import levenshteinDistance

diff = levenshteinDistance('Guacamole','Guecamole')

print(diff)
```
If you want to use the normalized metric, you can:

```python
from QLev import levN

diff = levN('Guacamole','Guecamole')

print(diff)
```
If you want to know the euclidian distance between two chars, you can:

```python
from QLev import qwertyDistance

diff = qwertyDistance('g','a')

print(diff)
```

To have a metric that uses the qwerty matrix between strings, you can:

```python
from QLev import qwertyN

diff = qwertyN('Guacamole','Guecamole')

print(diff)
```

To have a metric that uses levenshtein distance and the qwerty matrix between strings, you can:

```python
from QLev import QLev

diff = QLev('Guacamole','Guecamole')

print(diff)
```


## License

MIT License

Copyright (c) 2022 Alysson Amaral

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.