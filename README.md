CEDict_Parser
=============

CC-CEDICT is an English Chinese dictionary freely available for use in
applications and other such things. It can be downloaded here:
http://www.mdbg.net/chindict/chindict.php?page=cc-cedict

This Python 3 module parses a CEDict file, and returns a list of objects with
following attributes:
```python
self.traditional
self.simplified
self.pinyin
self.definition
```

Usage:
```python
from CEDICT_Parser.parser import *


parser = CEDictParser()

words = parser.parse_file("data/cedict_ts.u8")
```
