#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


def getjson(filename, type_=True):
    fn = '/home/yuiant/offline/cnschema'
    if type_:
        fn = os.path.join(fn, 'type')
    else:
        fn = os.path.join(fn, 'property')

    with open(os.path.join(fn, filename)) as f:
        res = json.load(f)
    return res


def Normalize_cnschema_type(filename):
    save_dir = '/home/yuiant/offline/cnschema/cnschema/type'
    prefix = '/home/yuiant/offline/cnschema/type'
    with open(os.path.join(prefix, filename)) as f:
        ctype = json.load(f)

    rm_property = [
        '_group_type', '_layer', '_usage', '_node_label', '_url_root',
        '_url_schema'
    ]
    rm_pTree = [
        '_examples', '_layer', '_usage', 'descriptionZh', 'rdfs:comment',
        'wikidataName', 'wikidataUrl', 'wikipediaUrl'
    ]
    rm_pTree_properties = [
        '_layer', '_usage', 'descriptionZh', 'domainIncludes', 'rangeIncludes',
        'rdfs:comment', 'wikidataName', 'wikidataUrl', 'wikipediaUrl'
    ]
    for k in rm_property:
        ctype.pop(k)
    for pt in ctype['_pTree']:
        for k in rm_pTree:
            try:
                pt.pop(k)
            except:
                continue
        for pp in pt['_properties']:
            for kk in rm_pTree_properties:
                pp.pop(kk)
    with open(os.path.join(save_dir, filename), 'w') as f:
        json.dump(ctype, f, ensure_ascii=False)


def Normalize_cnschema_property(filename):
    save_dir = '/home/yuiant/offline/cnschema/cnschema/property'
    prefix = '/home/yuiant/offline/cnschema/property'
    with open(os.path.join(prefix, filename)) as f:
        p = json.load(f)
    rm = [
        '_group_property', '_layer', '_usage', '_node_label', '_url_root',
        '_url_schema'
    ]
    for k in rm:
        p.pop(k)
    with open(os.path.join(save_dir, filename), 'w') as f:
        json.dump(p, f, ensure_ascii=False)


if __name__ == '__main__':
    dirs = os.listdir('/home/yuiant/offline/cnschema/type')
    for filename in dirs:
        print(filename)
        Normalize_cnschema_type(filename)
    dirs1 = os.listdir('/home/yuiant/offline/cnschema/property')
    for filename1 in dirs1:
        print(filename1)
        Normalize_cnschema_property(filename1)
