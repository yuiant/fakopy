#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from KB.model.knowledge import *
from pymongo import MongoClient
import pandas as pd
if __name__=='__main__':
    client = MongoClient('localhost',27017)
    db = client['block_chain_data']
    tb_coininfo = db['coin_information']
    tb_concept = db['fei_xiao_hao_concept']
    tb_crunchbase = db['crunchbase_companies']

    coininfo =pd.DataFrame(list(tb_coininfo.find()))

    concept = pd.DataFrame(list(tb_concept.find()))
    crunchbase = pd.DataFrame(list(tb_crunchbase.find()))




