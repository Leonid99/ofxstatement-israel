#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

VERSION = "0.0.1"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-israel',
      version=VERSION,
      author="Leonid Podolny",
      author_email="leonid@podolny.net",
      url="https://github.com/kedder/ofxstatement",
      description=("Sample plugin for ofxstatement"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['isracard1 = ofxstatement.plugins.isracard1:Isracard1Plugin',
          'hapoalim = ofxstatement.plugins.hapoalim:HapoalimPlugin']
          },
      install_requires=['ofxstatement', 'configparser', 'beautifulsoup4', 'lxml', 'python-dateutil', 'openpyxl'],
      include_package_data=True,
      zip_safe=True
      )
