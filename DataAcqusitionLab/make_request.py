"""
> cd "/Applications/Python 3.7/"
> sudo "./Install Certificates.command"
"""


import urllib.request 
import urllib.parse
import time
import os
import sys


def call_nooa(offset):
    params = urllib.parse.urlencode(
        {
            'limit': 1000,
            'offset': offset
        }
    )
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?%s" % params

    req = urllib.request.Request(url)
    req.add_header('Token', sys.argv[1])

    res = urllib.request.urlopen(req)
    return res


def write_result(data, file_name):
    file_path = os.path.join("./", "data", file_name)
    with open(file_path, "wb") as d:
        d.write(data)


def wait(secs):
    time.sleep(secs)


if __name__ == '__main__':
    offsets = [x for x in range(1, 39000, 1000)]
    file_names = ["locations_{0}.json".format(str(x - 1)[:1] if len(str(x)) < 5 else str(x)[:2]) for x in offsets]

    for file_name, offset in zip(file_names, offsets):
        data = call_nooa(offset)
        write_result(data, file_name)
        wait(5)
