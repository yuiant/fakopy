#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pyhanlp import *

def extract_triple(res):
    pass

def printpd(sentence):
    res = HanLP.parseDependency(sentence)
    ar = res.wordArray
    for a in ar:
        print(a.ID,a.CPOSTAG,a.POSTAG,a.LEMMA,a.DEPREL,a.HEAD.ID)

def parseTriple(res):
    wa = res.wordArray
    keyRelation = [a for a in wa if a.DEPREL=='核心关系'][0]
    SBV = [a for a in wa if a.HEAD.ID == keyRelation.ID and a.DEPREL=='主谓关系'][0]
    VOB = [a for a in  wa if a.HEAD.ID == keyRelation.ID and a.DEPREL=='动宾关系'][0]
    arrow = '===>'
    print(SBV.NAME,arrow,keyRelation.NAME,arrow,VOB.NAME)




if __name__ == '__main__':
    text = '据Coindesk消息，一名名为MelissaSweet的性工作者在三年前已经开始接受数字货币作为工作报酬，但通常情况下，她会立即将其转化为法币，而去年她开始使用数字货币作为退休储蓄。'
    text1 = 'MelissaSweet1表示，越来越多的银行认为任何性工作都是高风险的所以\
        拒绝接受色情行业公司的直接存款，因而她将数字货币纳入考虑范围之内。'

    text2 = '我洗了头发，现在准备吹干它。'


