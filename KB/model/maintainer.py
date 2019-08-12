#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from abc import ABCMeta, abstractmethod
from .knowledge import Entity, Property, Relation, Type


class Maintainer():
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self.path = path

    def load(self, T, short_dir, id_key='name'):
        path = os.path.join(self.path, short_dir)
        files = os.listdir(path)
        res = []
        for f in files:
            with open(os.path.join(path, f)) as f:
                j = json.load(f)
                res.append(T(**j))
        return dict(zip([getattr(x, id_key) for x in res], res))

    @abstractmethod
    def create(self, **kw):
        pass

    @abstractmethod
    def validate(self, **kw):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def query(self):
        pass


class CoreMaintainer(Maintainer):
    def __init__(self, path):
        super(CoreMaintainer, self).__init__(path)
        self.types = self.load(
            T=Type, short_dir=os.path.join('ontology', 'types'))
        self.properties = self.load(
            T=Property, short_dir=os.path.join('ontology', 'properties'))
        self.entities = self.load(
            T=Entity, short_dir=os.path.join('instance', 'entities'))
        self.relations = self.load(
            T=Relation, short_dir=os.path.join('instance', 'relations'))

    def create(self, **kw):
        category = kw.get('category')
        T = None
        if category == 'type':
            T = Type
            name = kw.get('name')
            new_properties = kw.pop('add_properties', None)
            super_ = kw.pop('add_super', None)
            parent = self.types.get(super_)
            kw.update({'super_': [x + [name] for x in parent.super_]})
            if new_properties:
                parent.properties.insert(0, {name: new_properties})
            kw.update({'properties': parent.properties})
            kw.update({'_id': os.path.join(kw.get('context'), name)})
        elif category == 'property':
            T = Property
        elif category == 'entity':
            T = Entity
            super_ = kw.get('super_')
            parent = self.types.get(super_)
            properties = [{
                list(x.keys())[0]:
                dict.fromkeys(list(x.values())[0], None)
            } for x in parent.properties]
            _id = os.path.join(kw.get('context'), 'entities', kw.get('name'))
            kw.update({'properties': properties, '_id': _id})
        elif category == 'relation':
            T = Relation
        print(kw)
        return T(**kw)

    def validate(self, **kw):
        return True

    def delete(self, **kw):
        pass

    def query(self, name):
        return [
            x
            for x in list(self.types.values()) + list(self.properties.values())
            + list(self.entities.values()) + list(self.relations.values())
            if name.lower() in [
                str(y).lower() for y in x.alternateName + [x.name, x.nameZh]
                if y
            ]
        ]

    def save(self, thing):
        path = None
        if thing.category == 'type':
            path = os.path.join(self.path, 'ontology', 'types')
        elif thing.category == 'property':
            path = os.path.join(self.path, 'ontology', 'properties')
        elif thing.category == 'entity':
            path = os.path.join(self.path, 'instance', 'entities')
        elif thing.category == 'relation':
            path = os.path.join(self.path, 'instance', 'relations')
        filepath = os.path.join(path, thing.name) + '.json'
        with open(filepath, 'w') as f:
            json.dump(thing.__dict__, f, ensure_ascii=False)
            return True
