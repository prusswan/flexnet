## Python 3

Ported to Python 3. Tested to work with FME 2014 (FlexServer 11.11)

Both `query_everything` and `report_everything` should work without errors:


    ./test.py


## Python 2 (older notes before the port)

Originally branched from https://github.com/ressy/flexnet

Must be in python2.7 environment. Check https://github.com/ressy/flexnet/issues/2

```
module load anaconda/5.0.1
source activate flexnet_py27
```

if pycrc is not found. check https://github.com/ressy/flexnet/issues/1

```
git clone https://github.com/ressy/flexnet.git
wget https://pycrc.org/download/pycrc-0.9.tar.gz
tar xzvf pycrc-0.9.tar.gz
PYTHONPATH=pycrc-0.9 python -c 'import flexnet' # no errors, hopefully?
```

It is not working at this moment for parsing server reponse though:

<pre>
# Traceback (most recent call last):
#   File "./test.py", line 9, in <module>
#   c.query_everything()
#   File ".../flexnet_lliu/flexnet/flexnet/client.py", line 330, in query_everything
#   self.query_vendor_details()
#   File ".../flexnet_lliu/flexnet/flexnet/client.py", line 415, in query_vendor_details
#   vendors[vendor_name]["hostname"] = msg["vendor_hostname"]
#   KeyError: 'vendor_hostname'
</pre>
