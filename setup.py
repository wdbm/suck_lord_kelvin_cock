#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():
    setuptools.setup(
        name                 = 'slokc',
        version              = '2020.01.07.1953',
        description          = 'Kelvin Building automated Wi-Fi login program',
        long_description     = long_description(),
        url                  = 'https://github.com/wdbm/suck_lord_kelvin_cock',
        author               = 'Will Breaden Madden',
        author_email         = 'wbm@protonmail.ch',
        license              = 'GPLv3',
        packages             = setuptools.find_packages(),
        install_requires     = [
                               'docopt'
                               ],
        entry_points         = {
                               'console_scripts': ('suck_lord_kelvin_cock = slokc.__init__:main')
                               },
        include_package_data = True,
        zip_safe             = False
    )

def long_description(filename='README.md'):
    if os.path.isfile(os.path.expandvars(filename)):
      try:
          import pypandoc
          long_description = pypandoc.convert_file(filename, 'rst')
      except ImportError:
          long_description = open(filename).read()
    else:
        long_description = ''
    return long_description

if __name__ == '__main__':
    main()
