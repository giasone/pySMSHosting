#!/usr/bin/env python

#from distutils.core import setup
#from setuptools import setup, find_packages
import sys, os

__license__ = 'GPL v.2 http://www.gnu.org/licenses/gpl.txt'
__author__ = "Gianluca Urgese <g.urgese@jasone.it>"
__version__ = '0.4'

# Distutils version
METADATA = dict(
	name = "pysmshosting",
	version = __version__,
	py_modules = ['smshosting'],
	author="Gianluca Urgese",
    author_email="g.urgese@jasone.it",
	description='Python Wrapper Library for Smshosting.it SOAP API',
	long_description= open("README").read(),
	license=__license__,
	url='http://github.com/giasone/pySMSHosting',
	keywords='Suse Studio wrapper python library api',
	packages=['smshosting'],

)

# Setuptools version
SETUPTOOLS_METADATA = dict(
	install_requires = ['setuptools', 'simplejson', 'suds'],
	include_package_data = True,
	zip_safe=True,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GPL License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet',
	]
)

def Main():
	try:
		import setuptools
		METADATA.update(SETUPTOOLS_METADATA)
		setuptools.setup(**METADATA)
	except ImportError:
		import distutils.core
		distutils.core.setup(**METADATA)

if __name__ == '__main__':
  Main()