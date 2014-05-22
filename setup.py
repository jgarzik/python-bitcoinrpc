#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-bitcoinrpc',
    version='0.1',
    description='Enhanced version of python-jsonrpc for use with Bitcoin',
    long_description=open('README.rst').read(),
    author='Jeff Garzik',
    author_email='<jgarzik@exmulti.com>',
    maintainer='Jeff Garzik',
    maintainer_email='<jgarzik@exmulti.com>',
    url='http://www.github.com/jgarzik/python-bitcoinrpc',
    packages=['bitcoinrpc'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
