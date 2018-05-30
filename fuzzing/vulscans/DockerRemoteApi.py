# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://drops.wooyun.org/papers/15892


import requests
import Queue
import traceback
import argparse
import threading
import json
import urlparse


class DockerRemoteApi():
    def __init__(self):
        self.result = []
        self.path = '/version'
        self.match = 'ApiVersion'
        self.port = '2375'
        self.q = Queue.Queue()

    def action(self, url):
        try:
            host = urlparse.urlparse(url).netloc
            self.q.put(r"http://" + host + ":" + self.port)
        except:
            traceback.print_exc()

    def Fuzz(self):
        try:
            while not self.q.empty():
                try:
                    url = self.q.get(block=False)
                except:
                    break
                try:
                    url = url + self.path
                    print url
                    r = requests.get(url, timeout=10)
                    content = r.content
                except:
                    content = ""
                if self.match in content:
                    self.result.append(url)
        except:
            traceback.print_exc()

    def Scan(self, info):
        try:
            if isinstance(info, str):
                self.action(info)
            else:
                for i in info:
                    self.action(i['url'])
            threads = []
            for i in xrange(10):
                t = threading.Thread(target=self.Fuzz,)
                t.start()
                threads.append(t)
            for i in threads:
                i.join()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", '--url', dest="url")
    parse.add_argument("-f", "--file", dest="file", default=None)
    parse.add_argument("-p", "--port", dest='port', default='2375')
    args = parse.parse_args()
    url = args.url
    file = args.file
    port = args.port
    if file:
        with open(file) as f:
            urls = json.loads(f.read())
    info = url if url else urls
    exa = DockerRemoteApi()
    exa.port = port
    exa.Scan(info)
    print exa.result
