# coding=utf-8
"""
WordChange - Одно изменение слова, которая составляет историю изменения слова
    affix = название аффикса, который был применен
    attrs - абрибуты слова по трем координатам
    index - индекс начала аффикса в слове
"""


class WordChange(object):
    def __init__(self, affix, index, attrs=None):
        self.affix = affix
        self.attrs = attrs
        self.index = index

    def __unicode__(self):
        return u"%s %s" % (unicode(self.affix), (u"("+unicode(self.attrs)+u")" if self.attrs else u""))

    def __str__(self):
        return self.__unicode__()
