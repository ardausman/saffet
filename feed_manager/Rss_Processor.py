import feedparser
import ssl
import time


class RSSProcessor:
    '''Variables'''
    ssl_cert = None

    '''Constructor'''
    def __init__(self):
        if hasattr(ssl, '_create_unverified_context'):  # aims to solve the SSL certficate issue (python requirement)
            ssl._create_default_https_context = ssl._create_unverified_context

    '''Methods'''
    @staticmethod
    def get_rss_feed(url):
        result = []
        time_interval = None
        '''Get Latest RSS Feed'''
        feed = feedparser.parse(url)
        '''Get Desired Info from it'''
        for entry in feed.entries:
            if "published_parsed" in entry:
                time_interval = time.time() - time.mktime(entry['published_parsed'])
            elif "updated_parsed" in entry:
                time_interval = time.time() - time.mktime(entry['updated_parsed'])
            if time_interval < 86400:
                tmp = dict()
                tmp['title'] = entry['title']
                if "published" in entry:
                    tmp['published'] = entry['published']
                elif "updated" in entry:
                    tmp['published'] = entry['published']
                if 'feedburner_origlink' in entry:
                    tmp['link'] = entry['feedburner_origlink']
                else:
                    tmp['link'] = entry['link']
                result.append(tmp)
        return result
