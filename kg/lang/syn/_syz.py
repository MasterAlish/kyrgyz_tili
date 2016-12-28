# coding=utf-8
from kg.lang.affix import Affix


class SyzZatMuchosu(Affix):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [SyzZatMuchosu.make]

    mucholor = [
        [u"сыз", u"суз", u"сиз", u"сүз"],
        [u"сыз", u"суз", u"сиз", u"сүз"],
        [u"сыз", u"суз", u"сиз", u"сүз"],
        [u"сыз", u"суз", u"сиз", u"сүз"],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            return self.word_object.word + mucho
        return self.word_object.word