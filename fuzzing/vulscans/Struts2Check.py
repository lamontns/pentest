# -*- coding:utf-8 -*-
# !/usr/bin/env python


import traceback
import requests
import Queue
import threading
import json
import argparse


class Struts2Check():
    def __init__(self):
        self.result = []
        self.q = Queue.Queue()
        self.path = 'struts2payload.json'

    def getpayload(self, url):
        try:
            if '.action' or '.do' in url:
                nurl = url.split('?')[0]
            else:
                return False
            for i in self.payload:
                for j in i['payload']:
                    if j['method'] == 'get':
                        nurl = nurl + j['payload']
                        self.q.put({"type": i['type'], "url": nurl,
                                    "data": "", "match": j["match"]})
                    if j['method'] == 'post':
                        data = j['payload']
                        self.q.put({"type": i["type"], "url": nurl,
                                    "data": data, "match": j["match"]})
        except:
            traceback.print_exc()

    def Fuzz(self):
        try:
            while not self.q.empty():
                try:
                    info = self.q.get(block=False)
                except:
                    break
                url = info['url']
                data = info['data']
                if data:
                    headers = {}
                    headers["Content-Type"]="application/x-www-form-urlencoded"
                    try:
                        print "Post url :" + url
                        print "data :" + data
                        r = requests.post(url, data=data, timeout=10)
                        content = r.content
                    except:
                        content = ""
                else:
                    try:
                        print "Requests url :" + url
                        r = requests.get(url, timeout=10)
                        content = r.content
                    except:
                        content = ""
                if info['match'].encode('utf-8') in content:
                    self.result.append(info)
        except:
            traceback.print_exc()

    def Scan(self, info):
        try:
            with open(self.path) as f:
                self.payload = json.loads(f.read())
            if isinstance(info, str):
                self.getpayload(info)
            else:
                for i in info:
                    self.getpayload(i['url'])
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
    parse.add_argument("-u", "--url", dest="url")
    parse.add_argument("-f", "--file", dest="file")
    args = parse.parse_args()
    url = args.url
    file = args.file
    if file :
        with open(file) as f:
            urls = json.loads(f.read())
    info = url if url else urls
    exa = Struts2Check()
    exa.Scan(info)
    if exa.result:
        print "*******************"
        print "exsit vul"
        print "*******************"
        print exa.result
