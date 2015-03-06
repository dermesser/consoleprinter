# coding=utf-8
"""
appinstance
Active8 (04-03-15)
license: GNU-GPL2
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from setuptools import setup
setup(name='consoleprinter',
      version='16',
      description='Console printer with linenumbers, stacktraces, logging, conversions and coloring..',
      url='https://github.com/erikdejonge/consoleprinter',
      author='Erik de Jonge',
      author_email='erik@a8.nl',
      license='GPL',
      packages=['consoleprinter'],
      zip_safe=True,
      install_requires=['ujson'],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 4 - Beta ",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: POSIX",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System",
      ])
