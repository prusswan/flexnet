#!/usr/bin/env python

import sys
from IPython import embed
sys.path.append('./pycrc-0.9')
import flexnet

c = flexnet.client.ManagerClient('ediliclan.ad.cirrus.com', port=5280)
c.query_everything()
embed()
