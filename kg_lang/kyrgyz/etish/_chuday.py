# coding=utf-8
from kg_lang.kyrgyz.feature import Feature


class ChudayEtishMuchosu(Feature):
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [ChudayEtishMuchosu.make]

    mucholor = [
        [u"чудай", u"чудай", u"чүдөй", u"чүдөй"],
        [u"чудай", u"чудай", u"чүдөй", u"чүдөй"],
        [u"чудай", u"чудай", u"чүдөй", u"чүдөй"],
        [u"чудай", u"чудай", u"чүдөй", u"чүдөй"]
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
            end_of_result = mucho
            return start_of_result + end_of_result
        return self.word_object.word
