#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-bitcoinrpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Bitcoin',
    long_description=open('README.rst').read(),
    author='Jeff Garzik',
    author_email='<jgarzik@pobox.com>',
    maintainer='Jeff Garzik',
    maintainer_email='<jgarzik@pobox.com>',
    url='http://www.github.com/jgarzik/python-bitcoinrpc',
    packages=['bitcoinrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
