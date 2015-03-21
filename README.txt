CEDict_Parser
=============

CC-CEDICT is an English Chinese dictionary freely available for use in
applications and other such things. It can be downloaded here:
http://www.mdbg.net/chindict/chindict.php?page=cc-cedict

This module parses the CEDict file, and returns a list of objects with
following attributes:
```
self.traditional
self.simplified
self.pinyin
self.definition
```

Usage:
```
from CEDICT_Parser.parser import *


parser = CEDictParser()

file_name = os.path.join(dir, "data/cedict_ts.u8")

words = parser.parse_file(file_name)
```