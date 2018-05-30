# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://www.wooyun.org/bugs/wooyun-2010-0196160


import traceback
import logging
import requests
import re
import json
import argparse
from gevent.threadpool import ThreadPool


class ELExpression():
    def __init__(self):
        self.result = []
        self.pool = ThreadPool(10)
        self.q = []
        self.payload = '{1000-121}'
        self.match = '879'

    def putinqueue(self, info):
        try:

            url = info[0]
            data = info[1]
            current = data if data else url
            for k in re.finditer(r'\=(?P<value>.*?)(?:$|&)', current):
                value = k.group('value')
                payload = current.replace(value, self.payload)
                if data:
                    self.q.append((url, payload))
                else:
                    self.q.append((payload, data))
        except:
            traceback.print_exc()

    def Fuzz(self, info):
        try:
            url = info[0]
            data = info[1]
            if data:
                try:
                    r = requests.post(url, data=data, timeout=10, verify=False)
                    content = r.content
                except:
                    content = ''
            else:
                try:
                    print "Req ::" + url
                    r = requests.get(url, timeout=10, verify=False)
                    content = r.content
                except:
                    content = ''
                if self.match in content:
                    msg = 'find vulnerable url'
                    logging.info(msg)
                    self.result.append(info)
        except:
            traceback.print_exc()

    def Scan(self, info):
        try:
            if isinstance(info, tuple):
                self.putinqueue(info)
            else:
                with open(info) as f:
                    ud = json.loads(f.read())
                for i in ud:
                    self.putinqueue(i)
            self.pool.map(self.Fuzz, self.q)
        except:
            traceback.print_exc()

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', '--url', dest='url')
    parse.add_argument('-d', '--data', dest='data', default=None)
    parse.add_argument('-f', '--file', dest='file')
    args = parse.parse_args()
    url = args.url
    data = args.data
    file = args.file
    info = (url, data) if url else file
    exa = ELExpression()
    exa.Scan(info)
    if exa.result:
        print exa.result
