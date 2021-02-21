#!/usr/bin/env python

import sys
from IPython import embed
sys.path.append('./pycrc-0.9')
import flexnet

# c = flexnet.client.ManagerClient('ediliclan.ad.cirrus.com', port=5280)
c = flexnet.client.ManagerClient('localhost', port=27000, debug=False)
# c = flexnet.client.ManagerClient('ML', port=27001, debug=False)
# c = flexnet.client.ManagerClient('ML', port=27009, debug=False, single_server=True) # to use main host for all queries

# c.query_everything()
c.report_everything()
