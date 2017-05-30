#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# suck_lord_kelvin_cock                                                        #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is an automated Wi-Fi login program.                            #
#                                                                              #
# copyright (C) 2017 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    program [options]

options:
    -h, --help       display help message
    --version        display version and exit
    --passcode=TEXT  passcode [default: none]
"""

import datetime
import docopt
import urllib
import urllib2

name    = "suck_lord_kelvin_cock"
version = "2017-05-30T1330Z"

def main(options):

    passcode = options["--passcode"]

    if passcode == "none":

        passcodes = {
                        "2017-12": "7b7281",
                        "2017-11": "f52186",
                        "2017-10": "f24a7b",
                        "2017-09": "d6ea48",
                        "2017-08": "a10b95",
                        "2017-07": "e900b2",
                        "2017-06": "a312b2",
                        "2017-05": "dfae91",
                        "2017-04": "9db408",
                        "2017-03": "3e0c66",
                        "2017-02": "ef54b1",
                        "2017-01": "04e300",
                        "2016-12": "c17cdf",
                        "2016-11": "d9866f",
                        "2016-10": "635847",
                        "2016-09": "7193ba",
                        "2016-08": "2be179",
                        "2016-07": "a02ca9",
                        "2016-06": "14b74f",
                        "2016-05": "ee3531",
                        "2016-04": "a23179",
                        "2016-03": "901043",
                        "2016-02": "420394",
                        "2016-01": "b0e0a4",
                        "2015-12": "74d339",
                        "2015-11": "a6deac",
                        "2015-10": "f3a509",
                        "2015-09": "8f56e4",
                        "2015-08": "0e0166",
                        "2015-07": "e03ae7",
                        "2015-06": "5d92f1",
                        "2015-05": "8c8f07",
                        "2015-04": "9540b4",
                        "2015-03": "843c3b",
                        "2015-02": "2ddf49",
                        "2015-01": "54b71b",
                        "2014-12": "a9385f",
                        "2014-11": "6d667e",
                        "2014-10": "4e4882",
                        "2014-09": "18c5ee",
                        "2014-08": "ca6de0",
                        "2014-07": "87cc03",
                        "2014-06": "01728d",
                        "2014-05": "137934",
                        "2014-04": "cb7df5",
                        "2014-03": "0a1d90",
                        "2014-02": "a03c01",
                        "2014-01": "5be672",
                        "2013-12": "89e1b4",
                        "2013-11": "ebc797",
                        "2013-10": "e71572",
                        "2013-09": "b42ec2",
                        "2013-08": "4db980",
                        "2013-07": "168003",
                        "2013-06": "7e6c0c",
                        "2013-05": "5925fd",
                        "2013-04": "adc888",
                        "2013-03": "0d8a74",
                        "2013-02": "671512",
                        "2013-01": "07e640",
                        "2012-12": "b4fa99",
                        "2012-11": "2507bb",
                        "2012-10": "cc825e",
                        "2012-09": "10cf6e",
                        "2012-08": "72037e",
                        "2012-07": "ae3d6a",
                        "2012-06": "845cd3",
                        "2012-05": "92c6b1",
                        "2012-04": "74c471",
                        "2012-03": "c01c97",
                        "2012-02": "cab747",
                        "2012-01": "3a65d6",
                        "2011-12": "6bddd7",
                        "2011-11": "bdc478",
                        "2011-10": "7095b2",
                        "2011-09": "a776c7",
                        "2011-08": "651fb2",
                        "2011-07": "1718df",
                        "2011-06": "e17142",
                        "2011-05": "94e0c3",
                        "2011-04": "a98b5c",
                        "2011-03": "c4b9c9",
                        "2011-02": "8a4080",
                        "2011-01": "67dcea"
        }

        date_current = datetime.datetime.utcnow().strftime("%Y-%m")

        if date_current in passcodes:

            passcode = passcodes[date_current]

        else:

            print("passcode not found -- consult DMT entities")
            exit()

    URL  = "http://start.ubuntu.com/wless/index.php"
    data = urllib.urlencode({"pin": passcode, "action": "auth"})

    response = ""

    try:

        response = urllib2.urlopen(URL, data)
        response = response.read()

    except urllib2.HTTPError as error_code:

        if error_code == 404:

            print("error 404 -- already logged in, dicknips?")
            exit()

    else:

        print("error -- fuck knows")
        exit()

    if "Correct" in response:

        print("login successful -- use this power wisely")

    else:

        print("login unsuccessful or already logged in or some other fucking "
              "error -- kill yourself")

if __name__ == "__main__":

    options = docopt.docopt(__doc__)
    if options["--version"]:

        print(version)
        exit()

    main(options)