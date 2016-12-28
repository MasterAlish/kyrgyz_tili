# coding=utf-8
from kg.lang.affix import Affix
from kg.lang.lang import WordEndingTypes
from types import LambdaType


class San(Affix):
    illegal_prev_affixes = ['taandyk']

    def __init__(self, word_object):
        """:type word_object: kg_lang.kyrgyz.lang.KyrgyzWord """
        self.word_object = word_object
        self.word_object.prepare()

    def transformers(self):
        if self.word_object.last_affix() in self.illegal_prev_affixes:
            return []
        return [San.koptuk]

    mucholor = [
            [u"лар", (u"лор", u"лар"), u"лер", u"лөр"],
            [u"дар", (u"дор", u"дар"), u"дер", u"дөр"],
            [u"лар", (u"лор", u"лар"), u"лер", u"лөр"],
            [u"тар", (u"тор", u"тар"), u"тер", u"төр"],
    ]

    def koptuk(self):
        if self.word_object.last_affix() in self.illegal_prev_affixes:
            return self.word_object
        if self.is_special_word():
            try:
                result, index = self.special_conversion()
                return self.word_object.change(result[:index], result[index:], "koptuk")
            except KeyError:
                pass

        if self.word_object.unsuz_end_type and self.word_object.unduu_type:
            i_unsuz, i_unduu = Affix.indexes[self.word_object.unsuz_end_type][self.word_object.unduu_type]
            mucho = self.mucholor[i_unsuz][i_unduu]
            end_of_result = mucho
            if isinstance(end_of_result, tuple):
                if self.word_object.unduu_type_jaaktuu:
                    end_of_result = end_of_result[0]
                else:
                    end_of_result = end_of_result[1]
            return self.word_object.change(self.word_object.word, end_of_result, "koptuk")
        return self.word_object

    def is_special_word(self):
        special_words = [u'бала', u'мен', u'сен', u'ал', u'ол', u'биз', u'силер', u'сиздер', u'алар', u'бул', u'булар',
                         u'ушул', u'ушулар']
        return not self.word_object.is_name and self.word_object.word in special_words

    def special_conversion(self):
        special_conversions = {u'бала': (u'балдар', 3),
                               u'мен': (u'биз', 0),
                               u'сен': (u'силер', 2),
                               u'ал': (u'алар', 1),
                               u'ол': (u'олор', 1),
                               u'биз': (u'биз', 0),
                               u'силер': (u'силер', 2),
                               u'сиздер': (u'сиздер', 3),
                               u'алар': (u'алар', 1),
                               u'бул': (u'булар', 2),
                               u'булар': (u'булар', 2),
                               u'ушул': (u'ушулар', 3),
                               u'ушулар': (u'ушулар', 3)}
        return special_conversions[self.word_object.word]
