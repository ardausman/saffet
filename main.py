# -*- coding: utf-8 -*-
import pprint
import re
from feed_manager import otx_processor

if __name__ == '__main__':
    otx = otx_processor.OTXProcessor()
    otx_iocs = otx.get_feed_from_otx()
    pprint.pprint(otx_iocs[0])
