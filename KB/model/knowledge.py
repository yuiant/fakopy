#! /usr/bin/env python
# -*- coding: utf-8 -*-

CONTEXT = 'http://404.ai'


class Thing():
    def __init__(self, **kw):
        self.context = kw.pop('context', CONTEXT)
        self.name = kw.pop('name', None)
        self.nameZh = kw.pop('nameZh', None)
        self.alternateName = kw.pop('alternateName', [])
        self.description = kw.pop('description', None)
        self.descriptionZh = kw.pop('descriptionZh', None)
        self.sameAs = kw.pop('sameAs', None)
        self.category = kw.pop('category', None)
        self.nlpTags = kw.pop('nlpTags', None)
        self.externalReference = kw.pop('externalReference', None)

    def __repr__(self):
        return '{0}:{1},{2}'.format(self.__class__, self.name, self.nameZh)


class Type(Thing):
    def __init__(self, **kw):
        super(Type, self).__init__(**kw)
        self.super_ = kw.pop('super_')
        self.properties = kw.pop('properties')
        self._id = kw.pop('_id')


class Property(Thing):
    def __init__(self, **kw):
        super(Property, self).__init__(**kw)
        # domain & range is a list of str
        self.domainIncludes = kw.pop('domainIncludes', [])
        self.rangeIncludes = kw.pop('rangeIncludes', [])


class Entity(Thing):
    def __init__(self, **kw):
        super(Entity, self).__init__(**kw)
        self.super_ = kw.pop('super_')
        self.properties = kw.pop('properties', None)
        self._id = kw.pop('_id')


class Relation(Thing):
    def __init__(self, **kw):
        super(Relation, self).__init__(**kw)
        self.super_ = kw.pop('super_')
        self._id = kw.pop('_id')
