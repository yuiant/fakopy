#! /usr/bin/env python
# -*- coding: utf-8 -*-

from KB.model.maintainer import CoreMaintainer
from pymongo import MongoClient
import pandas as pd

path = './data/core'
cm = CoreMaintainer(path)
client = MongoClient('127.0.0.1',27017)
db = client['block_chain_data']

def addType():
    conference = cm.create(category='type',name='Conference_',nameZh='会议',
                           alternateName=['会晤','谈判'],add_super='Event',context='http://404.ai')
    Industry = cm.create(category='type',name='Industry_',nameZh='行业',
              alternateName=['产业','工业'],add_super='Intangible',context='http://404.ai')

    Platform = cm.create(category='type',name='Platform_',nameZh='平台',
              alternateName=[],add_super='Intangible',context='http://404.ai')

    exchange = cm.create(category='type',name='Exchange_',nameZh='交易所',
              alternateName=[],add_super='Organization',context='http://404.ai')

    conceptBlock = cm.create(category='type',name='ConceptBlock_',nameZh='概念板块',
              alternateName=[],add_super='Intangible',context='http://404.ai')

    cryptocurrency = cm.create(category='type',name='CryptoCurrency_',nameZh='数字货币',
              alternateName=['虚拟货币'],add_super='CreativeWork',context='http://404.ai')

    blockchain = cm.create(category='type',name='BlockChain_',nameZh='区块链',
              alternateName=['链圈','链技术'],add_super='CreativeWork',context='http://404.ai')

    algorithm = cm.create(category='type',name='Algorithm_',nameZh='算法',
              alternateName=[''],add_super='CreativeWork',context='http://404.ai')

    [cm.save(x) for x in [conference,Platform,exchange,conceptBlock,cryptocurrency,
                          blockchain,algorithm]]


def addCoinInfo():
    colletion = db['coin_information']
    df = pd.DataFrame(list(colletion.find()))
    for i in range(0,df.shape[0]):
        series = df.iloc[i]
        coin = cm.create(context = 'http://404.ai',category = 'entity',
                         super_='CryptoCurrency_',name=series['code'],
                         nameZh=series['cnName'],descriptionZh=series['intro'],
                         alternateName=[series['shortName'],series['code']],
                         externalReference=[series['website'],series['blockSite']])
        cm.save(coin)
    platform = df['tokenPlatform'].dropna()
    for p in platform:
        _p = cm.create(context='http://404.ai',category='entity',
                       super_='Platform_',name=p+'_platform')
        cm.save(_p)


def addConcept():
    collection = db['fei_xiao_hao_concept']
    df = pd.DataFrame(list(collection.find()))
    for i in range(0,df.shape[0]):
        series = df.iloc[i]
        concept = cm.create(context='http://404.ai',category='entity',
                            super_='ConceptBlock_',name=series['code']+'_concept',
                            alternateName=[series['conceptName']])
        cm.save(concept)

def addCrunch():
    collection = db['crunchbase_companies']
    df = pd.DataFrame(list(collection.find()))
    orgs=[]
    people=[]
    place=[]

    for i in range(0,df.shape[0]):
        company = df.iloc[0]
        overview = company['overview']
        org = cm.create(context='http://404.ai/',category='entity',name=overview['name'].strip(),
                  description=overview['intro'],super_='Organization')
        orgs.append(org)
        for _addr in ['addr1','addr2']:
            addr = overview[_addr]
            if addr:
                _loc = cm.create(context='http://404.ai',category='entity',name=addr,super_='Place')
                place.append(_loc)
        currentTeam = company['currentTeam']
        if currentTeam:
            currentMB = company['currentTeam']['currentTeamMembers']
            for cmb in currentMB:
                person = cm.create(context='http://404.ai',category='entity',
                               name=cmb['name'],super_='Person')
                people.append(person)
    [cm.save(o) for o in orgs]
    [cm.save(p) for p in people]
    [cm.save(p) for p in place]





if  __name__ =='__main__':
    # addType()
    addCoinInfo()
    addConcept()
    addCrunch()
