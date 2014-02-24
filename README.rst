=================
python-bitcoinrpc
=================

AuthServiceProxy is an improved version of python-jsonrpc.

It includes the following generic improvements:

* HTTP connections persist for the life of the AuthServiceProxy object
* sends protocol 'version', per JSON-RPC 1.1
* sends proper, incrementing 'id'
* uses standard Python json lib

It also includes the following bitcoin-specific details:

* sends Basic HTTP authentication headers
* parses all JSON numbers that look like floats as Decimal



Installation
============

1. change the first line of setup.py to point to the directory of your installation of python 2.*
2. run setup.py

Note: This will only install bitcoinrpc. If you also want to install jsonrpc to preserve 
backwards compatibility, you have to replace 'bitcoinrpc' with 'jsonrpc' in setup.py and run it again.

Or simply install the library using pip::

    pip install python-bitcoinrpc



Example
=======
.. code:: python

    from bitcoinrpc.authproxy import AuthServiceProxy
    access = AuthServiceProxy("http://user:password@127.0.0.1:8332")
    access.getinfo()
    access.listreceivedbyaddress(6)
    access.sendtoaddress("11yEmxiMso2RsFVfBcCa616npBvGgxiBX", 10)
