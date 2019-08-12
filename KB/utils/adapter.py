#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
from abc import ABCMeta, abstractmethod


class Adapter():
    def __init__(self, **kw):
        self.source = kw.pop('source')
        self.target = kw.pop('target')


class Convertor():
    __metaclass__ = ABCMeta

    def __init__(self, **kw):
        self.source = kw.pop('source')
        self.target = kw.pop('target')

    def load(self):
        pass

    def read(self, input):
        pass

    def save(self, input):
        pass

    def convert(self, input):
        pass

    @abstractmethod
    def run(self,filename):
        pass


class CnschemaTypeConvertor(Convertor):
    def __init__(self, **kw):
        super(CnschemaTypeConvertor, self).__init__(**kw)
        self.load()

    def load(self):
        core_file = os.path.join(self.source, 'cns-core.jsonld')
        with open(core_file) as f:
            self.core = json.load(f)

    def read(self, input):
        output = None
        with open(os.path.join(self.source, input)) as f:
            output = json.load(f)
        return output

    def convert(self, input):
        pass

    def run(self,filename):
        with open(os.path.join(self.source,'types',filename)) as f:
            j = json.load(f)
        c = [x for x in self.core['@graph'] if x['name']==j['rdfs:label']][0]
        kw = dict(context='http://404.ai',
                  name = c['name'],
                  nameZh = c['nameZh'],
                  alternateName = c['alternateName'],
                  description = c['description'],
                  descriptionZh = c['descriptionZh'],
                  sameAs = c['supersededBy'],
                  category = 'type',
                  nlpTags=None,
                  externalReference = {'schema':{'schemaorgUrl':c['schemaorgUrl'],
                                                 'cnschemaUrl':c['@id']},
                                       'wiki':{'wikidataName':c['wikidataName'],
                                               'wikidataUrl':c['wikidataUrl'],
                                               'wikipediaUrl':c['wikipediaUrl']}},
                  super_=[[y['rdfs:label'] for y in z] for z in [x['_path'] for x in j['_paths']]],
                  _id = os.path.join('http://404.ai',c['name']),
                  properties = [{x['rdfs:label']:[y['rdfs:label'] for y in x['_properties']]} for x in j['_pTree']]

                  )
        with open(os.path.join(self.target,filename),'w') as f:
            json.dump(kw,f,ensure_ascii=False)



class CnscehmaPropertyConvertor(Convertor):
    def __init__(self,**kw):
        super(CnscehmaPropertyConvertor,self).__init__(**kw)
        self.load()
    def load(self):
        core_file = os.path.join(self.source, 'cns-core.jsonld')
        with open(core_file) as f:
            self.core = json.load(f)
    def run(self,filename):
        with open(os.path.join(self.source,'properties',filename)) as f:
            j = json.load(f)
        c = [x for x in self.core['@graph'] if x['name']==j['rdfs:label']][0]
        kw = dict(context='http://404.ai',
                  name = c['name'],
                  nameZh = c['nameZh'],
                  alternateName = c['alternateName'],
                  description = c['description'],
                  descriptionZh = c['descriptionZh'],
                  sameAs = c['supersededBy'],
                  category = 'property',
                  nlpTags=None,
                  externalReference = {'schema':{'schemaorgUrl':c['schemaorgUrl'],
                                                 'cnschemaUrl':c['@id']},
                                       'wiki':{'wikidataName':c['wikidataName'],
                                               'wikidataUrl':c['wikidataUrl'],
                                               'wikipediaUrl':c['wikipediaUrl']}},
                  _id = os.path.join('http://404.ai',c['name']),
                  domainIncludes =[x['rdfs:label'] for x in j.pop('domainIncludes',[])],
                  rangeIncludes =[x['rdfs:label'] for x in j.pop('rangeIncludes',[])]
                  )
        with open(os.path.join(self.target,filename),'w') as f:
            json.dump(kw,f,ensure_ascii=False)


