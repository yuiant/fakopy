#! /usr/bin/env python
# -*- coding: utf-8 -*-

from requests_html import HTMLSession
from .knowledge import *

BABEL_KEY='ee59fb3a-c274-42c8-8548-651ee3f96ef7'


# PREFIX={'zhishi.me':'http://zhishi.me/api/entity/',
#         'cndbpedia':'http://shuyantech.com/api/cndbpedia/ment2ent?q=',
#         'concpetNetZh':'http://api.conceptnet.io/c/zh/',
#         'conceptNetEn':'http://api.conceptnet.io/c/en/'}




# need to rebuild,未考虑稳定性
class engine():
    def __init__(self,**kw):
        self.session = HTMLSession()

    def search(self,cn_words):
        return self.parse_things(cn_words)
    def getBnUrl(self,lemma,lang):
        return 'https://babelnet.io/v5/getSenses?lemma={0}&searchLang={1}&key={2}'.format(lemma,lang,BABEL_KEY)

    def getZsUrl(self,cn_words):
        return 'http://zhishi.me/api/entity/'+cn_words


    def parse_things(self,cn_words):
        return self.parse_babel(cn_words)+[self.parse_zs(cn_words)]

    def parse_zs(self,cn_words):
        zsm = self.session.get(self.getZsUrl(cn_words)).json()
        zw = zsm['zhwiki']
        kw = dict(alternateName = zw['infobox']['\u20021'],
                  descriptionZh= zw['abstracts'],externalReference = zw['externalLink'])
        return Thing(**kw)

    def parse_babel(self,cn_words):
        babel = self.session.get(self.getBnUrl(lemma=cn_words,lang='Zh')).json()
        return [self._parse_babel(b) for b in babel]

    def _parse_babel(self,d):
        kw = dict(nameZh = d['properties']['fullLemma'])
        return Thing(**kw)



