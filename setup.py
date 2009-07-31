#! python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='pyedittag',
      version=version,
      description="MP3 tag editor",
      long_description="""\
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sumi Tomohiko',
      author_email='tom@nekomimists.ddo.jp',
      url='http://d.hatena.ne.jp/SumiTomohiko',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "tagpy", 
      ],
      entry_points={
          "console_scripts": ["pyedittag = pyedittag:main"], 
          }, 
      )

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop=4
