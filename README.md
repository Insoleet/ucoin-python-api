#ucoin-python-api

A python implementation of [uCoin](https://github.com/c-geek/ucoin) API

## Requirements

In order to use the API, you have to first install the required dependencies given below thanks to pip3:
 * requests
 * python-gnupg

##Installation

Here is a fast installation procedure (a bit dirty) we suggest to quickly use this API.

```bash
$ mkdir $HOME/ucoin
$ cd $HOME/ucoin
$ git clone git@github.com:canercandan/ucoin-python-api.git ucoinpy
$ export PYTHONPATH="$HOME/ucoin:$PYTHONPATH"
```

Thus you are ready to use it with your own python program. Here is an example illustrating how to use it thanks to the python shell:

```python
In [1]: import ucoinpy

In [2]: ucoinpy.ucg.Peering(server='mycurrency.candan.fr').get()
Out[2]:
{'contract': {'currentNumber': '5',
  'hash': 'FB710AE30F843BF505ABF9DE8CF404B7F35D238A'},
 'currency': 'mycurrency',
 'key': '6282C3F765E560992113137AD149AFF1B07FF751',
 'merkles': {'hdc/amendments/current/votes': {'depth': 1,
   'leavesCount': 2,
   'nodesCount': 1,
   'root': '2CEC90DEBBB89C10B6AB5EAEF17FF1D0BA8B4346'},
  'pks/all': {'depth': 2,
   'leavesCount': 4,
   'nodesCount': 3,
   'root': '944D0A3A0593C4B627BA41F0454BB4A705918CE9'}},
 'remote': {'host': 'mycurrency.candan.fr',
  'ipv4': '62.210.131.202',
  'ipv6': '',
  'port': 8081}}
```

Please take a look at the document [HTTP API](https://github.com/c-geek/ucoin/blob/master/doc/HTTP_API.md) to learn about the API.
