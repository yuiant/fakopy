#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from KB.utils.adapter import CnschemaTypeConvertor,CnscehmaPropertyConvertor
from KB.model.knowledge import *
from pymongo import MongoClient
import pandas as pd
def generate_entity():
    client = MongoClient('localhost',27017)
    db = client['block_chain_data']
    tb_coininfo = db['coin_information']
    tb_concept = db['fei_xiao_hao_concept']
    tb_crunchbase = db['crunchbase_companies']

    coininfo =pd.DataFrame(list(tb_coininfo.find()))

    concept = pd.DataFrame(list(tb_concept.find()))
    crunchbase = pd.DataFrame(list(tb_crunchbase.find()))





if __name__ == '__main__':
    ctc = CnschemaTypeConvertor(source = './data/external/cnschema',
                                 target='./data/core/ontology/types')
    for d in os.listdir(os.path.join(ctc.source,'types')):
        ctc.run(d)
        print(d)

    cpc =CnscehmaPropertyConvertor(source = './data/external/cnschema',
                                target='./data/core/ontology/properties')
    for d in os.listdir(os.path.join(cpc.source,'properties')):
        cpc.run(d)
        print(d)


