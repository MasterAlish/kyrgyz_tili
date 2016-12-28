# coding=utf-8
from kg_lang.kyrgyz.feature import Feature


class BaEtishMuchosu(Feature):
    """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord"""
    def __init__(self, word_object):
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        return [BaEtishMuchosu.make]

    mucholor = [
        [u"ба", (u"бо", u'ба'), u"бе", u"бө"],
        [u"ба", (u"бо", u'ба'), u"бе", u"бө"],
        [u"ба", (u"бо", u'ба'), u"бе", u"бө"],
        [u"па", (u"по", u'па'), u"пе", u"пө"],
    ]

    def make(self, jak=1, jeke=True, sylyk=False):
        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            index_i, index_j = self.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[index_i][index_j]
            start_of_result = self.word_object.word + u""
            end_of_result = mucho
            if isinstance(end_of_result, tuple):
                if self.word_object.unduu_type_jaaktuu:
                    end_of_result = end_of_result[0]
                else:
                    end_of_result = end_of_result[1]
            return self.word_object.change(start_of_result, end_of_result, 'ba')
        return self.word_object
