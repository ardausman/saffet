# -*- coding: utf-8 -*-
import requests
from datetime import date, datetime
import time


class OTXProcessor:
    ''' Variables '''
    apikey = "e2eca20eda34af9e4380ee7b2ef684cc3a81b4856d055909f0be16bfe2245b99"

    '''Methods'''
    def get_feed_from_otx(self):
        results = []
        # Prepare Request
        today = date.today()
        query = ['modified_since={0}'.format(today.strftime('%Y-%m-%dT%H%3A%M%3A%S.%f')), 'limit=20']
        # query.append('modified_since=2020-04-06T00%3A00%3A00+00%3A00')
        request_args = '&'.join(query)
        request_args = '?{}'.format(request_args)
        uri = "https://otx.alienvault.com/api/v1/pulses/subscribed{0}".format(request_args)
        response = requests.get(uri, verify=False, headers={"Content-Type": "application/json",
                                                            "X-OTX-API-KEY": self.apikey}, allow_redirects=False)
        # Process Response
        if response.status_code == 200:
            temp_results = response.json()
            for r in temp_results['results']:
                if (datetime.now() - datetime.strptime(r['created'].split('T')[0],'%Y-%m-%d')).total_seconds() < 86400:
                    tmp = dict()
                    if len(r['references']) > 0:
                        tmp['references'] = r['references'][0]
                    else:
                        tmp['references'] = "None"
                    tmp['name'] = r['name']
                    tmp['otx_id'] = r['id']
                    tmp['published'] = r['created']
                    results.append(tmp)
        else:
            return response.status_code
        return results
