#! /usr/bin/env python
# -*- coding: utf-8 -*-

from requests_html import HTMLSession
from wikidata.client import Client

BABEL_KEY='ee59fb3a-c274-42c8-8548-651ee3f96ef7'







cnKBs = ['zhishi.me','cnDBpida','conceptNet']
enKBs = ['wikidata','DBPedial','msGraph','conceptNet','...']

if __name__ == '__main__':
    session = HTMLSession()
    cnword = '比特币'
    enword = 'bitcoin'
    # zhishi.me
    zsm =  session.get('http://zhishi.me/api/entity/'+cnword).json()
    cndb = session.get('http://shuyantech.com/api/cndbpedia/ment2ent?q='+cnword).json()
    cc_cn = session.get('http://api.conceptnet.io/c/zh/'+cnword).json()
    cc_en = session.get('http://api.conceptnet.io/c/en/'+enword).json()





