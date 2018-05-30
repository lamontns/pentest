# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://drops.wooyun.org/papers/16030

import argparse
import requests
import traceback
import json
import urlparse
from gevent.threadpool import ThreadPool
import random


class CouchDb():
    def __init__(self):
        self.pool = ThreadPool(10)
        self.result = []
        self.port = "5984"
        self.q = []
        self.randomstrs = ['a', 'k', 'b', 'v', 'd', 'f', 'e', 'g']
        self.path = '_utils/index.html'

    def Fuzz(self, info):
        try:
            url = info[0]
            port = info[1]
            host = urlparse.urlparse(url).netloc
            url = r'http://' + host + ":" + port
            rstr = "".join(random.sample(self.randomstrs, 5))
            url = url + r'/' + rstr
            try:
                print "Req::" + url
                r = requests.put(url, timeout=10)
                if 'ok' and 'true' in r.content:
                    self.result.append(info)
            except:
                pass
        except:
            pass

    def Scan(self, info):
        try:
            if isinstance(info, tuple):
                self.q.append(info)
            else:
                with open(file) as f:
                    content = json.loads(f.read())
                    for i in content:
                        self.q.append((i['url'], self.port))
            self.pool.map(self.Fuzz, self.q)
        except:
            traceback.print_exc()

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", dest="url")
    parse.add_argument("-p", "--port", dest="port", default="5984")
    parse.add_argument("-f", "--file", dest="file")
    args = parse.parse_args()
    url = args.url
    port = args.port
    file = args.file
    info = (url, port) if url else file
    exa = CouchDb()
    exa.Scan(info)
    if exa.result:
        print "exsit vul"
        print exa.result
