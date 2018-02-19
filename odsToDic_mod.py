#!usr/bin/python

__author__ = "pstragie"

import os
import json
from pyexcel_ods3 import get_data
from pyexcel_ods3 import save_data

class OdsToDic(path):
    def __init__(self):
        self.dataDict = {}
        self.folder = path

    def readFromFiles(self, folder):
        for dp, dn, fn in os.walk(folder):
            for f in fn:
                name, ext = os.path.splitext(f)
                if ext == ".ods":
                    data = get_data(os.path.join(folder, f))
                    print(json.dumps(data))



"""
Write to ods file
>>> from pyexcel_ods3 import save_data
>>> data = OrderedDict() # from collections import OrderedDict
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
>>> save_data("your_file.ods", data)

Read from ods file
>>> from pyexcel_ods3 import get_data
>>> data = get_data("your_file.ods")
>>> import json
>>> print(json.dumps(data))
{"Sheet 1": [[1, 2, 3], [4, 5, 6]], "Sheet 2": [["row 1", "row 2", "row 3"]]}

Write an ods to memory
>>> from pyexcel_ods3 import save_data
>>> data = OrderedDict()
>>> data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
>>> data.update({"Sheet 2": [[7, 8, 9], [10, 11, 12]]})
>>> io = StringIO()
>>> save_data(io, data)
>>> # do something with the io
>>> # In reality, you might give it to your http response
>>> # object for downloading

Read from an ods from memory
>>> # This is just an illustration
>>> # In reality, you might deal with ods file upload
>>> # where you will read from requests.FILES['YOUR_ODS_FILE']
>>> data = get_data(io)
>>> print(json.dumps(data))
{"Sheet 1": [[1, 2, 3], [4, 5, 6]], "Sheet 2": [[7, 8, 9], [10, 11, 12]]}

More info: https://github.com/pyexcel/pyexcel-ods3/blob/master/README.rst
"""