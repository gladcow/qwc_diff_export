"""
export block height,  solvetime and difficulty to csv file
"""

import sys
from qwc_api import QwertycoindJsonApi


def main(argv):
    url = "http://localhost:8197"
    if len(argv):
        url = argv[0]
    qwcd = QwertycoindJsonApi(url)
    height = qwcd.getheight()
    prev_ts = 0
    for i in range(0,  height):
        header = qwcd.getblockheaderbyheight(i)
        ts = int(header["timestamp"])
        solvetime = 0
        if prev_ts > 0:
            solvetime = ts - prev_ts
        print("{}, {}, {}".format(i, solvetime, header["difficulty"]))
        prev_ts = ts


if __name__ == "__main__":
    main(sys.argv[1:])
