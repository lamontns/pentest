# -*- coding:utf-8 -*-
# !/usr/bin/env python


import traceback
import argparse
import logging
import socket
import os
import json
import Queue
import threading
import urlparse


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s'
                           '[line:%(lineno)d]%(message)s',
                    datefmt='%a,%d,%b,%Y,%H:%M:%S')


class rsyns():
    def __init__(self):
        self.result = []
        self.q = Queue.Queue()

    def action(self, url):
        try:
            host = urlparse.urlparse(url).netloc
            ip = socket.gethostbyname(host)
            return ip
        except:
            traceback.print_exc()
            return ""

    def Fuzz(self):
        try:
            while not self.q.empty():
                ip = ""
                try:
                    ip = self.q.get(block=False)
                except:
                    break
                cmd = "rsync %s::" % ip
                output = os.popen(cmd)
                content = output.read().strip().strip('\n')
                if content:
                    self.result.append({ip: content})
        except:
            pass

    def Scan(self, info):
        try:
            logging.info("start getting ip according url")
            if isinstance(info, str):
                ip = self.action(info)
                if ip:
                    self.q.put(ip)
            else:
                for i in info:
                    ip = self.action(i['url'])
                    if ip:
                        self.q.put(ip)
            threads = []
            for i in xrange(10):
                t = threading.Thread(target=self.Fuzz,)
                t.start()
                threads.append(t)
            for i in threads:
                i.join()
        except:
            pass


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", dest="url")
    parse.add_argument("-f", "--file", dest="file")
    args = parse.parse_args()
    url = args.url
    file = args.file
    urls = []
    if file:
        with open(file) as f:
            urls = json.loads(f.read())
    exa = rsyns()
    info = url if url else urls
    exa.Scan(info)
    if exa.result:
        msg = " exsit vul ip "
        logging.info(msg)
        print exa.result
