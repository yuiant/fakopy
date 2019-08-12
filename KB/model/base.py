#! /usr/bin/env python
# -*- coding: utf-8 -*-
from .knowledge import *
from .maintainer import *
from .exEngine import engine


class KnowledgeBase():
    def __init__(self, path):
        self._maintainer = CoreMaintainer(path)
        self._se = engine()

    # need to rebuild
    # def load(self):
    #     dirs = [
    #         'ontology/types', 'ontology/properties', 'instance/entities',
    #         'instance/relations'
    #     ]
    #     paths = [os.path.join(self.path, x) for x in dirs]
    #     types = []
    #     properties = []
    #     entities = []
    #     relations = []
    #     for d in os.listdir(paths[0]):
    #         with open(os.path.join(paths[0], d)) as f:
    #             jt = json.load(f)
    #         types.append(Type(**jt))
    #     for d in os.listdir(paths[1]):
    #         with open(os.path.join(paths[1], d)) as f:
    #             jt = json.load(f)
    #         properties.append(Property(**jt))
    #     for d in os.listdir(paths[2]):
    #         with open(os.path.join(paths[2], d)) as f:
    #             jt = json.load(f)
    #         entities.append(Entity(**jt))
    #     for d in os.listdir(paths[3]):
    #         with open(os.path.join(paths[3], d)) as f:
    #             jt = json.load(f)
    #         relations.append(Relation(**jt))

    # self.ontology = Ontology(types=types, properties=properties)
    # self.instance = Instance(entities=entities, relations=relations)

    def getType(self, type_name):
        return self._maintainer.types.get(type_name, None)

    def getProperty(self, property_name):
        return self._maintainer.properties.get(property_name, None)

    def getEntity(self, entity_name):
        return self._maintainer.entities.get(entity_name, None)

    def query(self, word):
        return self._maintainer.query(word)

    def search(self, word):
        return self._se.search(word)

    # def getRelation(self, relation_name):
    #     res = None
    #     try:
    #         res = [
    #             x for x in self.instance.relations if x.name == relation_name
    #         ][0]
    #     except:
    #         pass
    #     return res
